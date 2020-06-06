# filename: server.py
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
from Crypto.Hash import SHA256


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
        self.session_key = None
        self.client_pubkey = None
        self.client_pubkey_len = None
        self.server_prikey = None

        #to decrypted saved password and prikey
        self.passphrase="sepfmp"
        self.iv = b'\x8c\xbcW\xcf\x0b\xa6\x00\xec\xa7\x94\xd2\x9a\x01Z\xd7\xfc'

        self.timeout = 30

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
            #self.server_prikey = RSA.import_key(open("private_keys/"+self.OWN_ADDR+".pem").read())
            cipher_rsa = PKCS1_OAEP.new(self.server_prikey)
            decrypted_nonce = cipher_rsa.decrypt(encrypted_nonce)

            #print("type_msg", type_msg)
            #print("msg_len",msg_len)
            #print("sender",sender_id)
            #print("recipient", recipient_id)
            #print("pubkey_a")
            #print(pubkey_a)
            #print("encrypted nonce")
            #print(encrypted_nonce)
            #print("sig")
            #print(sig)
            
            #update internal parameters
            self.DST_ADDR = sender_id
            return decrypted_nonce
        elif type_msg == self.protocols.sep_type2num('REQ_LOGIN'):
            encrypted_password = msg[16:-256]
            
            #decrypt password
            #self.server_prikey = RSA.import_key(open("private_keys/"+self.OWN_ADDR+".pem").read())
            cipher_rsa = PKCS1_OAEP.new(self.server_prikey)
            decrypted_password = cipher_rsa.decrypt(encrypted_password)
            return decrypted_password
        else:
            print("Error: unknown message type")
            return None

    def read_msg(self, msg):
        ver = msg[0]
        type_protocol = msg[1]
        print(ver)
        print(type_protocol)
        if type_protocol != self.protocols.protocol2num(self.current_protocol):
            print("Error: unexpected protocol type - received message protocol=" + type_protocol)
            return None, None, None

        if type_protocol == self.protocols.protocol2num("SEP"):
            return ver, type_protocol, self.read_SEP(msg)
        elif type_protocol == self.protocols.protocol2num("FMP"):
            pass
            #Todo: create self.read_FMP
            
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
            time.sleep(0.5)
    
    def start(self):
        self.load_server_prikey()
        session_key = None
        while True:
            session_key = self.connect()
            if session_key is not None:
                break
        print("Connection established with", self.DST_ADDR)
        #print(session_key)
        


if __name__ == '__main__':
    server = Server()
    server.start()
