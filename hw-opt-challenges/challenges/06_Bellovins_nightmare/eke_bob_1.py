import sys, getopt
import textbookRSA
from base64 import b64encode, b64decode
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.strxor import strxor

try:
    opts, args = getopt.getopt(sys.argv[1:],'hp:i:o:')
except getopt.GetoptError:
    print("Usage: eke_bob_1.py -p <password> -i <input_msg_file> -o <output_msg_file>")
    sys.exit(2)

password = ''
input_msg_file = 'eke_msg_1.txt'
output_msg_file = 'eke_msg_2.txt'

for opt, arg in opts:
    if opt == '-h':
        print("Usage: eke_bob_1.py -p <password> -i <input_msg_file> -o <output_msg_file>")
        sys.exit()
    elif opt == '-p':
        password = arg
    elif opt == '-i':
        if len(arg) != 0: input_msg_file = arg
    elif opt == '-o':
        if len(arg) != 0: output_msg_file = arg

f = open(input_msg_file, 'rb')
salt = b64decode(f.readline())
enc_exp_e = b64decode(f.readline())
modulus = b64decode(f.readline())
f.close()

pwdkey = PBKDF2(password, salt, dkLen=len(enc_exp_e), count=1000)
exp_e = strxor(enc_exp_e, pwdkey)

e = int(exp_e.decode('utf-8'))
if e%2 == 0: e -= 1
n = int(modulus.decode('utf-8'))

rsa = textbookRSA.TextbookRSA({'e':e, 'n':n, 'd':0})

session_key = get_random_bytes(16)
enc_session_key = rsa.encrypt(session_key)

f = open(output_msg_file, 'wb')
f.write(b64encode(str(enc_session_key).encode('utf-8')) + b'\n')
f.close()

f = open('sessionkey.txt', 'wb')
f.write(b64encode(session_key) + b'\n')
f.close()
