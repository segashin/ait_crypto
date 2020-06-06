# filename: server.py
# author: Shinsaku Segawa
# last modified: 2020/4/30

import os, sys, getopt, time, shutil
from pathlib import Path
from getpass import getpass
import secrets
from netinterface import network_interface
from protocols import Protocols
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256, HMAC
from Crypto.Util.Padding import pad, unpad

class Server():
    def __init__(self):
        self.ver = 1
        self.current_protocol = 'SEP' # changed to FMP later
        self.expected_incoming_msg_type = "REQ_INIT"
        self.OWN_ADDR = "Z"#input("Type your own address: ")
        print("Starting server as Z...")
        self.DST_ADDR = None
        self.NET_PATH = "./network"
        self.FOLDER_PATH = "./server"
        if (self.NET_PATH[-1] != '/') and (self.NET_PATH[-1] != '\\'): self.NET_PATH += '/'
        if (self.FOLDER_PATH[-1] != '/') and (self.FOLDER_PATH[-1] != '\\'): self.FOLDER_PATH += '/'
        self.netif = network_interface(self.NET_PATH, self.OWN_ADDR)
        self.protocols = Protocols()
        self.timeout = 30
        self.sleep_time = 0.1

        self.session_key = None

        self.client_pubkey = None
        self.client_pubkey_len = None
        self.server_prikey = None

        # to decrypted saved password and prikey
        self.passphrase="sepfmp"
        self.iv = b'\x8c\xbcW\xcf\x0b\xa6\x00\xec\xa7\x94\xd2\x9a\x01Z\xd7\xfc'

        #fmp seq num
        self.seq_last_received = 0
        self.seq_last_sent = 0

        #fmp file manipulation
        self.client_root_path = None
        self.cur_dir = None

    def load_server_prikey(self):
        try:
            key = open(self.FOLDER_PATH+"private_keys/"+self.OWN_ADDR+".pem", "rb").read()
            self.server_prikey = RSA.import_key(key, passphrase=self.passphrase)
        except:
            print("Error: could not load server private key")

    def fix_length(self, input_byte, desired_length):
        if(len(input_byte) > desired_length):
            print("Error fixing the length of byte")
            return
        res = b""
        for i in range(desired_length-len(input_byte)):
            res += b"\x00"
        res += input_byte
        return res

    def generate_session_key(self):
        return secrets.token_bytes(32)
    
    def mkpad(self, s, size):
        s = s.encode("utf-8")  # UTF-8文字列をバイト列に変換する
        pad = b' ' * (size - len(s) % size)  # 特定の長さの倍数にするための空白を生成
        return s + pad

    def verify_password(self, password):
        key = self.mkpad(self.passphrase, 16)
        cipher = AES.new(key, AES.MODE_CBC, self.iv)
        ctext = open(self.FOLDER_PATH+"password/"+self.DST_ADDR, "rb").read()
        correct_pwd = cipher.decrypt(ctext)
        correct_pwd = correct_pwd.strip(b" ")
        if correct_pwd == password:
            return True
        return False

    def gen_iv(self):
        return secrets.token_bytes(16)

    def SEP_ENC(self, ptext, key):
        cipher_rsa = PKCS1_OAEP.new(key)
        ctext = cipher_rsa.encrypt(ptext)
        return ctext
    
    def SEP_DEC(self, ctext, key):
        cipher_rsa = PKCS1_OAEP.new(key)
        ptext = cipher_rsa.decrypt(ctext)
        return ptext

    def SEP_SIGN(self, message, key):
        h = SHA256.new(message)
        signature = pkcs1_15.new(key).sign(h)
        return signature

    def SEP_GEN(self, ver, type_sep, type_msg, sender_id, recipient_id, encrypted_content, sig_key):
        msg = b""
        msg += ver
        msg += type_sep
        msg += type_msg
        msg += len(encrypted_content).to_bytes(length=5, byteorder='big') #msg_len
        msg += sender_id
        msg += recipient_id
        msg += encrypted_content
        sig = self.SEP_SIGN(msg, sig_key)
        #print("Generated sig: ")
        #print(sig)
        msg += sig
        return msg

    def SEP_RES_INIT(self, nonce):
        #header
        ver = self.ver.to_bytes(length=1, byteorder='big')
        type_sep = self.protocols.protocol2num("SEP").to_bytes(length=1, byteorder='big')
        type_msg = self.protocols.sep_type2num("RES_INIT").to_bytes(length=1, byteorder='big')
        sender_id = self.fix_length(self.OWN_ADDR.encode('utf-8'), 4)
        recipient_id = self.fix_length(self.DST_ADDR.encode('utf-8'), 4)

        #content - encrypted nonce
        ctext = self.SEP_ENC(nonce, self.client_pubkey)

        #send msg
        msg = self.SEP_GEN(ver, type_sep, type_msg, sender_id, recipient_id, ctext, self.server_prikey)
        self.netif.send_msg(self.DST_ADDR, msg)

    def SEP_RES_LOGIN(self, status, session_key=None):
        #header
        ver = self.ver.to_bytes(length=1, byteorder='big')
        type_sep = self.protocols.protocol2num("SEP").to_bytes(length=1, byteorder='big')
        type_msg = self.protocols.sep_type2num("RES_LOGIN").to_bytes(length=1, byteorder='big')
        sender_id = self.fix_length(self.OWN_ADDR.encode('utf-8'), 4)
        recipient_id = self.fix_length(self.DST_ADDR.encode('utf-8'), 4)
        login_status = None
        ctext = None
        if status:
            s = 1
            login_status = s.to_bytes(length=1, byteorder='big')
            ptext = login_status+session_key
            ctext = self.SEP_ENC(ptext, self.client_pubkey)
        else:
            s = 0
            login_status = s.to_bytes(length=1, byteorder='big')
            ctext = self.SEP_ENC(login_status, self.client_pubkey)
        
        msg = self.SEP_GEN(ver, type_sep, type_msg, sender_id, recipient_id, ctext, self.server_prikey)
        self.netif.send_msg(self.DST_ADDR, msg)

    def read_SEP(self, msg):
        type_msg = msg[2]
        if type_msg == self.protocols.sep_type2num(self.expected_incoming_msg_type):
            print("(OK): protocol type matches")
        else:
            print("Error: unexpected message type")
            return None
        msg_len = int.from_bytes(msg[3:8], 'big') #int
        if len(msg) == 16+msg_len+256:
            print("(OK): message length matches")
        else:
            print("Error: message length does not match")
            return None
        sender_id = msg[8:12].decode('utf-8').strip(chr(0)) #string
        if sender_id == self.DST_ADDR:
            print("(OK): correct sender address")
        else:
            print("Error: wrong sender address")
        recipient_id = msg[12:16].decode('utf-8').strip(chr(0)) #string
        if recipient_id == self.OWN_ADDR:
            print("(OK): correct recipient address")
        else:
            print("Error: wrong recipient address")
            return None

        if self.client_pubkey is None and type_msg == self.protocols.sep_type2num('REQ_INIT'):
            self.client_pubkey_len = int.from_bytes(msg[16:20], 'big')
            self.client_pubkey = RSA.import_key(msg[20:20+self.client_pubkey_len])

        #verify signature
        sig = msg[-256:]
        h = SHA256.new(msg[:-256])
        try:
            pkcs1_15.new(self.client_pubkey).verify(h, sig)
            print("(OK): sginature valid")
        except:
            print("Error: signature invalid")
            return

        if type_msg == self.protocols.sep_type2num('REQ_INIT'):
            encrypted_nonce = msg[20+self.client_pubkey_len:-256]
            
            #decrypt nonce
            cipher_rsa = PKCS1_OAEP.new(self.server_prikey)
            decrypted_nonce = cipher_rsa.decrypt(encrypted_nonce)

            #update internal parameters
            self.DST_ADDR = sender_id
            return decrypted_nonce
        elif type_msg == self.protocols.sep_type2num('REQ_LOGIN'):
            encrypted_password = msg[16:-256]
            
            #decrypt password
            cipher_rsa = PKCS1_OAEP.new(self.server_prikey)
            decrypted_password = cipher_rsa.decrypt(encrypted_password)
            return decrypted_password
        else:
            print("Error: unknown message type")
            return None

    def FMP_ENC(self, ptext):
        iv = self.gen_iv()
        len(self.session_key)
        cipher = AES.new(self.session_key, AES.MODE_CBC, iv=iv)
        ctext = cipher.encrypt(pad(ptext, AES.block_size))
        return iv, ctext
    
    def FMP_DEC(self, iv, ctext):
        cipher = AES.new(self.session_key, AES.MODE_CBC, iv=iv)
        ptext = unpad(cipher.decrypt(ctext), AES.block_size)
        return ptext

    def FMP_MAC(self, msg):
        h = HMAC.new(self.session_key, digestmod=SHA256)
        h.update(msg)
        return h.digest()

    def FMP_GEN(self, type_msg, content):
        ver = self.ver.to_bytes(length=1, byteorder='big')
        type_fmp = self.protocols.protocol2num("FMP").to_bytes(length=1, byteorder='big')
        type_msg = self.protocols.fmp_type2num(type_msg).to_bytes(length=1, byteorder='big')
        sender_id = self.fix_length(self.OWN_ADDR.encode('utf-8'), 4)
        recipient_id = self.fix_length(self.DST_ADDR.encode('utf-8'), 4)
        
        iv, encrypted_content = self.FMP_ENC(content)

        msg = b""
        msg += ver
        msg += type_fmp
        msg += type_msg
        msg += (len(iv) + len(encrypted_content)).to_bytes(length=5, byteorder=('big'))
        msg += sender_id
        msg += recipient_id
        msg += iv
        msg += encrypted_content
        mac = self.FMP_MAC(msg)
        msg += mac

        return msg

    def FMP_SEND(self, msg):
        self.netif.send_msg(self.DST_ADDR, msg)
        self.seq_last_sent += 1


    def FMP_MKD(self, content):
        dirname = content.decode('utf-8')
        dirnamealnum = dirname.replace("_", "")
        dirnamealnum = dirnamealnum.replace("-", "")

        if not dirnamealnum.isalnum():
            print("Error: invalid directory name")
            content = (self.seq_last_sent+1).to_bytes(2, 'big')
            content += (0).to_bytes(length=1, byteorder='big')
            msg = self.FMP_GEN("MKD",content)
            self.FMP_SEND(msg)
            print("FMP_MKD response sent")
            return
        
        try:
            os.makedirs(os.path.join(self.client_root_path, self.cur_dir, dirname), exist_ok=True)
        except:
            print("Error: could not make a new directory")
            content = (self.seq_last_sent+1).to_bytes(2, 'big')
            content += (0).to_bytes(length=1, byteorder='big')
            msg = self.FMP_GEN("MKD",content)
            self.FMP_SEND(msg)
            print("FMP_MKD response sent")
            return
        
        content = None
        content = (self.seq_last_sent+1).to_bytes(2, 'big')
        content += (1).to_bytes(length=1, byteorder='big')

        msg = self.FMP_GEN("MKD",content)
        self.FMP_SEND(msg)
        print("MKD: directory created")
        print("FMP_MKD response sent")
        return

    def FMP_RMD(self, content):
        dirname = content.decode('utf-8')
        dirnamealnum = dirname.replace("_", "")
        dirnamealnum = dirnamealnum.replace("-", "")

        if not dirnamealnum.isalnum():
            print("Error: invalid directory name")
            content = (self.seq_last_sent+1).to_bytes(2, 'big')
            content += (0).to_bytes(length=1, byteorder='big')
            msg = self.FMP_GEN("RMD",content)
            self.FMP_SEND(msg)
            print("FMP_RMD response sent")
            return
        
        try:
            shutil.rmtree(os.path.join(self.client_root_path, self.cur_dir, dirname))
        except:
            print("Error: could not delete directory")
            content = (self.seq_last_sent+1).to_bytes(2, 'big')
            content += (0).to_bytes(length=1, byteorder='big')
            msg = self.FMP_GEN("RMD",content)
            self.FMP_SEND(msg)
            print("FMP_RMD response sent")
            return

        content = (self.seq_last_sent+1).to_bytes(2, 'big')
        content += (1).to_bytes(length=1, byteorder='big')

        msg = self.FMP_GEN("RMD",content)
        self.FMP_SEND(msg)
        print("RMD: directory deleted")
        print("FMP_RMD response sent")
        return


    def FMP_GWD(self, content):
        content = (self.seq_last_sent+1).to_bytes(2, 'big')
        if len(self.cur_dir) > 0 and self.cur_dir[0] == ".":
            self.cur_dir = self.cur_dir[2:]
        cwd = self.DST_ADDR+":\\"+self.cur_dir
        content += cwd.encode('utf-8')

        msg = self.FMP_GEN("GWD", content)
        self.FMP_SEND(msg)
        print("FMP_GWD response sent")

    def FMP_CWD(self, content):

        dirname = content.decode('utf-8')
        dirnamealnum = dirname.replace("_", "")
        dirnamealnum = dirnamealnum.replace("-", "")

        if dirname == ".." and os.path.normpath(self.cur_dir) != os.path.normpath(""):
            pass
        elif not dirnamealnum.isalnum():
            print("Error: invalid destinatino directory")
            content = (self.seq_last_sent+1).to_bytes(2, 'big')
            content += (0).to_bytes(length=1, byteorder='big')
            msg = self.FMP_GEN("CWD",content)
            self.FMP_SEND(msg)
            print("FMP_CWD response sent")
            return
        elif not os.access(os.path.join(self.client_root_path, self.cur_dir, dirname), os.F_OK):
            print("Error: the destination path does not exist")
            content = (self.seq_last_sent+1).to_bytes(2, 'big')
            content += (0).to_bytes(length=1, byteorder='big')
            msg = self.FMP_GEN("CWD",content)
            self.FMP_SEND(msg)
            print("FMP_CWD response sent")
            return
        
        try:
            if dirname == "..":
                self.cur_dir = str(Path(self.cur_dir).parent)
            else:
                self.cur_dir = os.path.join(self.cur_dir, dirname)
        except:
            print("Error: could not change directory")
            content = (self.seq_last_sent+1).to_bytes(2, 'big')
            content += (0).to_bytes(length=1, byteorder='big')
            msg = self.FMP_GEN("CWD",content)
            self.FMP_SEND(msg)
            print("FMP_CWD response sent")
            return
        
        content = (self.seq_last_sent+1).to_bytes(2, 'big')
        content += (1).to_bytes(length=1, byteorder='big')

        msg = self.FMP_GEN("CWD",content)
        self.FMP_SEND(msg)
        print("CWD: current directory changed")
        print("FMP_CWD response sent")
        return

    def FMP_LST(self, content):
        content = (self.seq_last_sent+1).to_bytes(2, 'big')
        dirlist = os.listdir(os.path.join(self.client_root_path, self.cur_dir))

        dirlist_text = ""
        for item in dirlist:
            dirlist_text += item+","
        content += dirlist_text.encode('utf-8')

        msg = self.FMP_GEN("LST", content)
        self.FMP_SEND(msg)
        print("FMP_LST response sent")

    def FMP_UPL(self, content):

        fname_len = int.from_bytes(content[:2], 'big')
        decoded_content = content[2:].decode('utf-8')
        fname = decoded_content[:fname_len]
        fcont = decoded_content[fname_len:]

        fnamealnum = fname.replace("_", "")
        fnamealnum = fnamealnum.replace("-", "")
        fnamealnum = fnamealnum.replace(".", "")

        if not fnamealnum.isalnum():
            print("Error: invalid file name")
            content = (self.seq_last_sent+1).to_bytes(2, 'big')
            content += (0).to_bytes(length=1, byteorder='big')
            msg = self.FMP_GEN("UPL",content)
            self.FMP_SEND(msg)
            print("FMP_UPL response sent")
            return
        try:
            fname = os.path.join(self.client_root_path, self.cur_dir, fname)
            with open(fname, "w") as f: f.write(fcont)
        except:
            print("Error: could not make a file")
            content = (self.seq_last_sent+1).to_bytes(2, 'big')
            content += (0).to_bytes(length=1, byteorder='big')
            msg = self.FMP_GEN("UPL",content)
            self.FMP_SEND(msg)
            print("FMP_UPL response sent")
            return
        
        content = (self.seq_last_sent+1).to_bytes(2, 'big')
        content += (1).to_bytes(length=1, byteorder='big')

        msg = self.FMP_GEN("UPL",content)
        self.FMP_SEND(msg)
        print("UPL: file uploaded")
        print("FMP_UPL response sent")
        return

    def FMP_DNL(self, content):
        fname = content.decode('utf-8')
        try:
            f_cont = open(os.path.join(self.client_root_path, self.cur_dir, fname), "rb").read()
        except:
            print("Error: could not read the file")
            content = (self.seq_last_sent+1).to_bytes(2, 'big')
            content += (0).to_bytes(length=1, byteorder='big')
            msg = self.FMP_GEN("UPL",content)
            self.FMP_SEND(msg)
            print("FMP_DNL response sent")
            return
        
        content = (self.seq_last_sent+1).to_bytes(2, 'big')
        content += (1).to_bytes(length=1, byteorder='big')
        content += f_cont

        msg = self.FMP_GEN("DNL",content)
        self.FMP_SEND(msg)
        print("DNL: directory created")
        print("FMP_DNL response sent")
        return

    def FMP_RMF(self, content):
        fname = content.decode('utf-8')

        dirnamealnum = fname.replace("_", "")
        dirnamealnum = dirnamealnum.replace("-", "")
        dirnamealnum = dirnamealnum.replace(".", "")

        if not dirnamealnum.isalnum():
            print("Error: invalid directory name")
            content = (self.seq_last_sent+1).to_bytes(2, 'big')
            content += (0).to_bytes(length=1, byteorder='big')
            msg = self.FMP_GEN("RMF",content)
            self.FMP_SEND(msg)
            print("FMP_RMD response sent")
            return
        
        try:
            os.remove(os.path.join(self.client_root_path, self.cur_dir, fname))
        except:
            print("Error: could not remove the file")
            content = (self.seq_last_sent+1).to_bytes(2, 'big')
            content += (0).to_bytes(length=1, byteorder='big')
            msg = self.FMP_GEN("RMF",content)
            self.FMP_SEND(msg)
            print("FMP_RMF response sent")
            return
        
        content = (self.seq_last_sent+1).to_bytes(2, 'big')
        content += (1).to_bytes(length=1, byteorder='big')

        msg = self.FMP_GEN("RMF",content)
        self.FMP_SEND(msg)
        print("RMF: directory created")
        print("FMP_RMF response sent")
        return


    def FMP_END(self, content):
        content = (self.seq_last_sent+1).to_bytes(2, 'big')
        content += (1).to_bytes(length=1, byteorder='big')
        msg = self.FMP_GEN("END",content)
        self.FMP_SEND(msg)
        print("FMP_END response sent")
        print("END: session terminated")
        os.sys.exit(0)
        return
        
    def read_FMP(self, msg):
        type_command = msg[2]
        msg_len = int.from_bytes(msg[3:8], 'big') #int

        if len(msg) == 16+msg_len+32:
            print("(OK): message length matches")
        else:
            print("Error: message length does not match")
            return None
        sender_id = msg[8:12].decode('utf-8').strip(chr(0)) #string
        if sender_id == self.DST_ADDR:
            print("(OK): correct sender address")
        else:
            print("Error: wrong sender address")
        recipient_id = msg[12:16].decode('utf-8').strip(chr(0)) #string
        if recipient_id == self.OWN_ADDR:
            print("(OK): correct recipient address")
        else:
            print("Error: wrong recipient address")
            return None
        
        iv = msg[16:32]
        ctext = msg[32:-32]
        mac = msg[-32:]

        # verify mac
        h = HMAC.new(self.session_key, digestmod=SHA256)
        h.update(msg[:-32])
        try:
            h.verify(mac)
            print("(OK): MAC ok")
        except ValueError:
            print("Error: MAC verification failed")
            return None

        # decrypt
        ptext = self.FMP_DEC(iv, ctext)
        seq_num = int.from_bytes(ptext[0:2], byteorder='big')
        content = ptext[2:]

        # check seq_num
        if seq_num <= self.seq_last_received:
            print("Error: invalid sequence number")
            return None
        else:
            self.seq_last_received = seq_num
            print("(OK): sequence number ok")

        if type_command == self.protocols.fmp_type2num("MKD"):
            self.FMP_MKD(content)
        elif type_command == self.protocols.fmp_type2num("RMD"):
            self.FMP_RMD(content)
        elif type_command == self.protocols.fmp_type2num("GWD"):
            self.FMP_GWD(content)
        elif type_command == self.protocols.fmp_type2num("CWD"):
            self.FMP_CWD(content)
        elif type_command == self.protocols.fmp_type2num("LST"):
            self.FMP_LST(content)
        elif type_command == self.protocols.fmp_type2num("UPL"):
            self.FMP_UPL(content)
        elif type_command == self.protocols.fmp_type2num("DNL"):
            self.FMP_DNL(content)
        elif type_command == self.protocols.fmp_type2num("RMF"):
            self.FMP_RMF(content)
        elif type_command == self.protocols.fmp_type2num("END"):
            self.FMP_END(content)
        else:
            print("Error: unknown type_command")

    def read_msg(self, msg):
        ver = msg[0]
        type_protocol = msg[1]

        if type_protocol != self.protocols.protocol2num(self.current_protocol):
            print("Error: unexpected protocol type - received message protocol=" + type_protocol)
            return None, None, None

        if type_protocol == self.protocols.protocol2num("SEP"):
            return ver, type_protocol, self.read_SEP(msg)
        elif type_protocol == self.protocols.protocol2num("FMP"):
            return ver, type_protocol, self.read_FMP(msg)
            #Todo: create self.read_FMP
        else:
            print("Error: unexpected protocol")
            
    def connect(self):
        self.current_protocol = "SEP"
        self.expected_incoming_msg_type = "REQ_INIT"
        status = None
        msg = None
        # wait for SEP REQ_INIT
        self.expected_incoming_msg_type = "REQ_INIT"
        while True:
            status, msg = self.netif.receive_msg(blocking=True)
            print("SEP REQ_INIT received")
            ver, type_protocol, decrypted_nonce = self.read_msg(msg)
            if decrypted_nonce is not None:
                print("SEP REQ_INIT accepted")
                self.SEP_RES_INIT(decrypted_nonce)
                print("SEP RES_INIT sent")
                break
            else:
                print("Error: SEP REQ_INIT rejected")
                return None
        # wait for SEP REQ_LOGIN
        self.expected_incoming_msg_type = "REQ_LOGIN"
        stime = time.time()
        while True:
            status, msg = self.netif.receive_msg(blocking=False)
            if status:
                print("SEP REQ_LOGIN received")
                ver, type_protocol, password = self.read_msg(msg)
                if password is not None:
                    print("SEP REQ_LOGIN accepted")
                    # TODO SEP RES LOGIN
                    if self.verify_password(password):
                        print("(OK): password ok")
                        session_key = self.generate_session_key()
                        self.SEP_RES_LOGIN(True, session_key=session_key)
                        print("SEP RES_LOGIN sent")
                        return session_key
                    else:
                        print("(!!): password incorrect")
                        self.SEP_RES_LOGIN(False)
                        print("SEP RES_LOGIN sent")
                        continue # keep waiting for correct password
            #cehck request timeout
            etime = time.time()
            if (etime - stime > self.timeout):
                print("Connection request timed out:",self.timeout,"sec")
                return None
            time.sleep(self.sleep_time)

    def start(self):
        self.load_server_prikey()
        session_key = None
        while True:
            session_key = self.connect()
            if session_key is not None:
                break
        print("Connection established with", self.DST_ADDR)
        #print(session_key)
        self.current_protocol = "FMP"
        
        self.client_root_path = os.path.join(self.FOLDER_PATH, "client_data", self.DST_ADDR)
        self.cur_dir = ""
        self.session_key = session_key
        while True:
            status, msg = self.netif.receive_msg(blocking=True)
            print("FMP REQ received")
            self.read_msg(msg)

if __name__ == '__main__':
    server = Server()
    server.start()
