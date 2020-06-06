import sys, getopt
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util import Counter

try:
    opts, args = getopt.getopt(sys.argv[1:],'hi:')
except getopt.GetoptError:
    print("Usage: eke_bob_2.py -i <input_msg_file>")
    sys.exit(2)

input_msg_file = 'eke_msg_3.txt'

for opt, arg in opts:
    if opt == '-h':
        print("Usage: eke_bob_2.py -i <input_msg_file>")
        sys.exit()
    elif opt == '-i':
        if len(arg) != 0: input_msg_file = arg

f = open("sessionkey.txt", "rb")
session_key = b64decode(f.readline())
f.close()

f = open(input_msg_file, 'rb')
nonce = b64decode(f.readline())
enc_msg = b64decode(f.readline())
f.close()

ctr = Counter.new(64, prefix=nonce, initial_value=0)
aes_cipher = AES.new(session_key, AES.MODE_CTR, counter=ctr)

msg = aes_cipher.decrypt(enc_msg)
print(msg.decode('utf-8'))

