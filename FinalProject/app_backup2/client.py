# filename: client.py
# author: Shinsaku Segawa
# last modified: 2020/4/30

import os, sys, getopt, time
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

class Client():

    def __init__(self):
        self.current_protocol = "SEP" # changed to FMP later
        self.expected_incoming_msg_type = "RES_INIT"
        self.ver = 1
        self.NET_PATH = "./network"
        self.FOLDER_PATH = "./client"
        if (self.NET_PATH[-1] != '/') and (self.NET_PATH[-1] != '\\'): self.NET_PATH += '/'
        if (self.FOLDER_PATH[-1] != '/') and (self.FOLDER_PATH[-1] != '\\'): self.FOLDER_PATH += '/'
        self.DST_ADDR = None
        self.OWN_ADDR = input('Type your own address: ') # Ex. A, B, or C
        self.netif = network_interface(self.NET_PATH, self.OWN_ADDR)
        self.protocols = Protocols()
        self.timeout = 30
        self.sleep_time = 0.1

        self.session_key = None

        self.client_prikey = None
        self.client_pubkey = None
        self.server_pubkey = None

        #fmp seq num
        self.seq_last_received = 0
        self.seq_last_sent = 0

        self.DATA_LOC = "my_data"

    def clean_keys(self):
        self.client_prikey = None
        self.client_pubkey = None
        self.server_pubkey = None
    
    def load_client_prikey(self):
        try:
            key = open(self.FOLDER_PATH+"private_keys/"+self.OWN_ADDR+".pem", "rb").read()
            self.client_prikey = RSA.import_key(key)
        except:
            print("Error: could not load client private key")
    
    def load_client_pubkey(self):
        try:
            key = open(self.FOLDER_PATH+"public_keys/"+self.OWN_ADDR+".pem", "rb").read()
            self.client_pubkey = RSA.import_key(key)
        except:
            print("Error: could not load client public key")

    def load_server_pubkey(self):
        try:
            key = open(self.FOLDER_PATH+"public_keys/"+self.DST_ADDR+".pem", "rb").read()
            self.server_pubkey = RSA.import_key(key)
        except:
            print("Error: could not load server public key")
    
    def fix_length(self, input_byte, desired_length):
        if(len(input_byte) > desired_length):
            print("Error fixing the length of byte")
            return None
        res = b""
        for i in range(desired_length-len(input_byte)):
            res += b"\x00"
        res += input_byte
        return res

    def handle_options(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:], shortopts='hp:a', longopts=['help', 'path=', 'addr='])
        except getopt.GetoptError:
            print('wrong options')
            sys.exit(1)
    
    def generate_nonce(self):
        return secrets.token_bytes(32)

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


    def SEP_REQ_INIT(self):
        
        # generate SEP REQ_INIT
        #header
        ver = self.ver.to_bytes(length=1, byteorder='big')
        type_sep = self.protocols.protocol2num("SEP").to_bytes(length=1, byteorder='big')
        type_msg = self.protocols.sep_type2num("REQ_INIT").to_bytes(length=1, byteorder='big')
        sender_id = self.fix_length(self.OWN_ADDR.encode('utf-8'), 4)
        recipient_id = self.fix_length(self.DST_ADDR.encode('utf-8'), 4)
        
        #content
        nonce = self.generate_nonce()
        #pubkey_a = self.client_pubkey
        pubkey_a = self.client_pubkey.export_key()
        #with open("public_keys/"+self.OWN_ADDR+".pem", "rb") as f: pubkey_a = f.read()
        ctext = b""
        ctext += len(pubkey_a).to_bytes(length=4, byteorder='big')
        ctext += pubkey_a
        nonce_encrypted = self.SEP_ENC(nonce, self.server_pubkey)
        ctext += nonce_encrypted

        #send msg
        msg = self.SEP_GEN(ver, type_sep, type_msg, sender_id, recipient_id, ctext, self.client_prikey)
        self.netif.send_msg(self.DST_ADDR, msg)
        #print("Generated nonce: ")
        #print(nonce)
        #print("encrypted nonce: ")
        #print(nonce_encrypted)
        return nonce

    def SEP_REQ_LOGIN(self):
        password = getpass('Type your login password: ') # 8-16 letters
        if len(password)>16:
            print("Error: password must be less than 16 letters")
            return False
        # generate SEP REQ_INIT
        #header
        ver = self.ver.to_bytes(length=1, byteorder='big')
        type_sep = self.protocols.protocol2num("SEP").to_bytes(length=1, byteorder='big')
        type_msg = self.protocols.sep_type2num("REQ_LOGIN").to_bytes(length=1, byteorder='big')
        sender_id = self.fix_length(self.OWN_ADDR.encode('utf-8'), 4)
        recipient_id = self.fix_length(self.DST_ADDR.encode('utf-8'), 4)

        #keys to be used
        #server_public_key = RSA.import_key(open("public_keys/"+self.DST_ADDR+".pem").read())
        #client_private_key = RSA.import_key(open("private_keys/"+self.OWN_ADDR+".pem").read())

        #content
        ctext = self.SEP_ENC(password.encode('utf-8'), self.server_pubkey)

        #send msg
        msg = self.SEP_GEN(ver, type_sep, type_msg, sender_id, recipient_id, ctext, self.client_prikey)
        self.netif.send_msg(self.DST_ADDR, msg)
        return True

    def read_SEP(self, msg):
        type_msg = msg[2]
        if type_msg == self.protocols.sep_type2num(self.expected_incoming_msg_type):
            print("(OK): message type matches")
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
        recipient_id = msg[12:16].decode('utf-8').strip(chr(0)) #string
        if recipient_id == self.OWN_ADDR:
            print("(OK): correct recipient address")
        else:
            print("Error: wrong recipient address")
            return None

        # verify signature
        sig = msg[-256:]
        h = SHA256.new(msg[:-256])
        try:
            pkcs1_15.new(self.server_pubkey).verify(h, sig)
            print("(OK): signature valid")
        except:
            print("Error: signature invalid")
            return None

        if type_msg == self.protocols.sep_type2num('RES_INIT'):
            #client_private_key = RSA.import_key(open("private_keys/"+self.OWN_ADDR+".pem").read())
            #server_public_key = RSA.import_key(open("public_keys/"+self.DST_ADDR+".pem").read())
            encrypted_nonce = msg[16:-256]

            # decrypt nonce
            cipher_rsa = PKCS1_OAEP.new(self.client_prikey)
            decrypted_nonce = cipher_rsa.decrypt(encrypted_nonce)
            return decrypted_nonce
        elif type_msg == self.protocols.sep_type2num('RES_LOGIN'):
            encrypted_msg_content = msg[16:-256]

            # decrypt
            cipher_rsa = PKCS1_OAEP.new(self.client_prikey)
            decrypted_msg_content = cipher_rsa.decrypt(encrypted_msg_content)

            login_status = decrypted_msg_content[0]
            if login_status == 0:
                print("Error: login failed due to incorrect password")
                return None
            elif login_status == 1: # login sucess
                session_key = decrypted_msg_content[1:]
                print("(OK): password correct")
                return session_key
            else:
                print("Error: uknown response type")
        else:
            print("Error: unknown message type")
        return None
    
    def read_msg(self,msg):
        ver = msg[0]
        type_protocol = msg[1]

        if type_protocol != self.protocols.protocol2num(self.current_protocol):
            print("Error: unexpected protocol type - received message protocol=" + type_protocol)
            return None, None, None

        if type_protocol == self.protocols.protocol2num("SEP"):
            return ver, type_protocol, self.read_SEP(msg)
        elif type_protocol == self.protocols.protocol2num("FMP"):
            return ver, type_protocol, self.read_FMP(msg)

    def connect(self):
        self.DST_ADDR = input('Type a server address: ')
        self.load_client_prikey()
        self.load_client_pubkey()
        self.load_server_pubkey()
        # send SEP REQ_INIT
        nonce = None
        while True:
            nonce = self.SEP_REQ_INIT()
            if nonce is not None:
                print("SEP REQ INIT sent")
                break
        # wait for SEP RES_INIT
        self.expected_incoming_msg_type = "RES_INIT"
        stime = time.time()
        while True:
            status, msg = self.netif.receive_msg(blocking=False)
            if status:
                print("SEP RES_INIT received")
                ver, type_protocol, nonce_returned = self.read_msg(msg)
                if nonce == nonce_returned:
                    print("(OK): server verified")
                    print("SEP RES_INIT accpeted")
                    break
                else:
                    print("Error: server verification failed")
                    return None
            #check request timeout
            etime = time.time()
            if (etime - stime > self.timeout): # 20 sec timeout
                print("Connection request timed out:", self.timeout,"sec")
                return None
            time.sleep(self.sleep_time)

        while True:
            # send SEP REQ_LOGIN
            while True:
                res = self.SEP_REQ_LOGIN()
                if res:
                    break
            # wait for SEP RES_LOGIN
            self.expected_incoming_msg_type = "RES_LOGIN"
            stime = time.time()
            while True:
                status, msg = self.netif.receive_msg(blocking=False)
                if status:
                    print("SEP RES_LOGIN received")
                    ver, type_protocol, session_key = self.read_msg(msg)
                    if session_key is not None:
                        return session_key
                    else:
                        break
                etime = time.time()
                if (etime - stime > self.timeout):
                    print("Connection request timed out:", self.timeout,"sec")
                    return None
                time.sleep(self.sleep_time)

    def gen_iv(self):
        return secrets.token_bytes(16)

    def FMP_ENC(self, ptext):
        iv = self.gen_iv()
        len(self.session_key)
        cipher = AES.new(self.session_key, AES.MODE_CBC, iv=iv)
        ctext = cipher.encrypt(pad(ptext, AES.block_size))
        return iv, ctext

    def FMP_MAC(self, msg):
        h = HMAC.new(self.session_key, digestmod=SHA256)
        h.update(msg)
        return h.digest()

    def FMP_DEC(self, iv, ctext):
        cipher = AES.new(self.session_key, AES.MODE_CBC, iv=iv)
        ptext = unpad(cipher.decrypt(ctext), AES.block_size)
        return ptext

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
    
    def FMP_LISTEN(self, command):
        # wait for FMP RES
        self.expected_incoming_msg_type = command

        stime = time.time()
        while True:
            status, msg = self.netif.receive_msg(blocking=False)
            if status:
                print("FMP_"+command, "response received")
                ver, type_protocol, content = self.read_msg(msg)
                if content is not None:
                    return content
                else:
                    print("Error: response message invalid")
                    continue
            etime = time.time()
            if (etime - stime > self.timeout):
                print("Error: no response received")
                return None
            time.sleep(self.sleep_time)
        return None
    
    def FMP_SEND(self, msg):
        self.netif.send_msg(self.DST_ADDR, msg)
        self.seq_last_sent += 1
    
    def FMP_MKD(self):
        dir_name = input("Type directory name: ")

        # content
        # 2 bytes for seq num
        content = (self.seq_last_sent+1).to_bytes(2, 'big')
        content += dir_name.encode('utf-8')
        msg = self.FMP_GEN("MKD", content)
        self.FMP_SEND(msg)
        print("FMP_MKD request sent")

        res = self.FMP_LISTEN("MKD")
        res = int.from_bytes(res, 'big')
        if res == 0:
            print("Error: MKD failed")
        elif res == 1:
            print("MKD: directory created")
    
    def FMP_RMD(self):
        dir_name = input("Type directory name: ")
        confirm = input("All sub contents will be deleted: (y/n) ")
        if confirm != "y":
            print("RMD cancelled")
            return

        content = (self.seq_last_sent+1).to_bytes(2, 'big')
        content += dir_name.encode('utf-8')
        msg = self.FMP_GEN("RMD", content)
        self.FMP_SEND(msg)
        print("FMP_RMD request sent")

        res = self.FMP_LISTEN("RMD")
        res = int.from_bytes(res, 'big')
        if res == 0:
            print("Error: RMD failed")
        elif res == 1:
            print("RMD: directory deleted")
    
    def FMP_GWD(self):
        content = (self.seq_last_sent+1).to_bytes(2, 'big')
        msg = self.FMP_GEN("GWD", content)
        self.FMP_SEND(msg)
        print("FMP_GWD request sent")

        res = self.FMP_LISTEN("GWD")

        if res is not None:
            res = res.decode('utf-8')
            print(res)
    
    def FMP_CWD(self):
        dir_name = input("Type destination: ")

        # content
        # 2 bytes for seq num
        content = (self.seq_last_sent+1).to_bytes(2, 'big')
        content += dir_name.encode('utf-8')
        msg = self.FMP_GEN("CWD", content)
        self.FMP_SEND(msg)
        print("FMP_CWD request sent")

        res = self.FMP_LISTEN("CWD")
        res = int.from_bytes(res, 'big')
        if res == 0:
            print("Error: CWD failed")
        elif res == 1:
            print("CWD: current directory changed")
    
    def FMP_LST(self):
        content = (self.seq_last_sent+1).to_bytes(2, 'big')
        msg = self.FMP_GEN("LST", content)
        self.FMP_SEND(msg)
        print("FMP_LST request sent")

        res = self.FMP_LISTEN("LST")

        if res is not None:
            res = res.decode('utf-8')
            res = list(res.split(","))
            for i in res:
                print(i)
    
    def FMP_UPL(self):
        file_name = input("Type file name:")
        
        try:
            f_cont =  open(os.path.join(self.FOLDER_PATH , self.DATA_LOC , file_name), "rb").read()
        except:
            print("Error: failed to read the file")
            return

        # content
        # 2 bytes for seq num
        content = (self.seq_last_sent+1).to_bytes(2, 'big')
        content += len(file_name).to_bytes(2, ('big'))
        content += file_name.encode('utf-8')
        content += f_cont

        msg = self.FMP_GEN("UPL", content)
        self.FMP_SEND(msg)
        print("FMP_UPL request sent")

        res = self.FMP_LISTEN("UPL")
        res = int.from_bytes(res, 'big')
        if res == 0:
            print("Error: UPL failed")
        elif res == 1:
            print("UPL: file uploaded")
    
    def FMP_DNL(self):
        file_name = input("Type file name: ")

        content = (self.seq_last_sent+1).to_bytes(2, 'big')
        content += file_name.encode('utf-8')
        msg = self.FMP_GEN("DNL", content)
        self.FMP_SEND(msg)
        print("FMP_DNL request sent")

        res = self.FMP_LISTEN("DNL")

        fcont = res[1:].decode('utf-8')
        res = res[0]
        if res == 0:
            print("Error: DNL failed")
        elif res == 1:
            open(os.path.join(self.FOLDER_PATH, self.DATA_LOC, file_name), "w").write(fcont)
            print("DNL: file downloaded")

    def FMP_RMF(self):
        file_name = input("Type file name: ")
        content = (self.seq_last_sent+1).to_bytes(2, 'big')
        content += file_name.encode('utf-8')
        msg = self.FMP_GEN("RMF", content)
        self.FMP_SEND(msg)
        print("FMP_RMF request sent")

        res = self.FMP_LISTEN("RMF")

        res = int.from_bytes(res, 'big')
        if res == 0:
            print("Error: RMF failed")
        elif res == 1:
            print("RMF: file removed")
    
    def FMP_END(self):
        confirm = input("Disconnect and terminate session: (y/n)")
        if confirm != 'y':
            print("END cancelled")
            return
        content = (self.seq_last_sent+1).to_bytes(2, 'big')
        msg = self.FMP_GEN("END", content)
        self.FMP_SEND(msg)
        print("FMP_END request sent")
        res = self.FMP_LISTEN("END")

        res = int.from_bytes(res, 'big')
        if res == 0:
            print("Error: END failed")
        elif res == 1:
            os.sys.exit(0)
            print("END: session terminated")

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
        
        return content

    def fmp_process(self):
        command = input("Type command: ")
        if command == "MKD":
            self.FMP_MKD()
        elif command == "RMD":
            self.FMP_RMD()
        elif command == "GWD":
            self.FMP_GWD()
        elif command == "CWD":
            self.FMP_CWD()
        elif command == "LST":
            self.FMP_LST()
        elif command == "UPL":
            self.FMP_UPL()
        elif command == "DNL":
            self.FMP_DNL()
        elif command == "RMF":
            self.FMP_RMF()
        elif command == "END":
            self.FMP_END()
        else:
            print("Error: unknown command")

    def start(self):
        session_key = None
        while True:
            session_key = self.connect()
            if session_key is not None:
                break
        print("Connection established with", self.DST_ADDR)
        #print(session_key)

        self.current_protocol = "FMP"
        self.session_key = session_key
        self.seq_last_sent = 0

        while True:
            self.fmp_process()

if __name__ == '__main__':
    client = Client()
    client.start()