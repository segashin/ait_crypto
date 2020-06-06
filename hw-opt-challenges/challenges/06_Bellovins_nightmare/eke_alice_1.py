import sys, getopt, random
import textbookRSA
from base64 import b64encode, b64decode
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.strxor import strxor

try:
    opts, args = getopt.getopt(sys.argv[1:],'hp:o:')
except getopt.GetoptError:
    print("Usage: eke_alice_1.py -p <password> -o <output_msg_file>")
    sys.exit(2)

password = ''
output_msg_file = 'eke_msg_1.txt'

for opt, arg in opts:
    if opt == '-h':
        print("Usage: eke_alice_1.py -p <password> -o <output_msg_file>")
        sys.exit()
    elif opt == '-p':
        password = arg
    elif opt == '-o':
        if len(arg) != 0: output_msg_file = arg

rsa = textbookRSA.TextbookRSA()
keypair = rsa.getKey()

f = open('rsakeypair.txt', 'w')
f.write(str(keypair['e']) + '\n')
f.write(str(keypair['n']) + '\n')
f.write(str(keypair['d']) + '\n')
f.close()

#print('\nPublic key: ')
#print(keypair['e'])
#print(keypair['n'])
#print('\nPrivate key: ')
#print(keypair['d'])

exp_e = str(keypair['e']+random.randint(0,1)).encode('utf-8')
modulus = str(keypair['n']).encode('utf-8')

salt = get_random_bytes(8)
pwdkey = PBKDF2(password, salt, dkLen=len(exp_e), count=1000)

enc_exp_e = strxor(exp_e, pwdkey)

f = open(output_msg_file, 'wb')
f.write(b64encode(salt) + b'\n')
f.write(b64encode(enc_exp_e) + b'\n')
f.write(b64encode(modulus) + b'\n')
f.close()
