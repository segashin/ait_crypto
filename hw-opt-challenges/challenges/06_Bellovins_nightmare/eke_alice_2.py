import sys, getopt
import textbookRSA
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Random import get_random_bytes

try:
    opts, args = getopt.getopt(sys.argv[1:],'hi:o:')
except getopt.GetoptError:
    print("Usage: eke_alice_2.py -i <input_msg_file> -o <output_msg_file>")
    sys.exit(2)

input_msg_file = 'eke_msg_2.txt'
output_msg_file = 'eke_msg_3.txt'

for opt, arg in opts:
    if opt == '-h':
        print("Usage: eke_alice_2.py -i <input_msg_file> -o <output_msg_file>")
        sys.exit()
    elif opt == '-i':
        if len(arg) != 0: input_msg_file = arg
    elif opt == '-o':
        if len(arg) != 0: output_msg_file = arg

f = open("rsakeypair.txt", "r")
e = int(f.readline())
n = int(f.readline())
d = int(f.readline())
f.close()

rsa = textbookRSA.TextbookRSA({'e':e, 'n':n, 'd':d})

f = open(input_msg_file, 'rb')
enc_session_key = int(b64decode(f.readline()).decode('utf-8'))
f.close()

session_key = rsa.decrypt(enc_session_key)
nonce = get_random_bytes(8)
ctr = Counter.new(64, prefix=nonce, initial_value=0)
aes_cipher = AES.new(session_key, AES.MODE_CTR, counter=ctr)

msg = input("Type your message: ")
enc_msg = aes_cipher.encrypt(msg.encode('utf-8'))

f = open(output_msg_file, 'wb')
f.write(b64encode(nonce) + b'\n')
f.write(b64encode(enc_msg) + b'\n')
f.close()
