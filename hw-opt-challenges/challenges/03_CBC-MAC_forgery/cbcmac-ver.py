import sys, getopt
from Crypto.Cipher import AES

keystring = ''
inputfile = ''
macfile = ''

try:
    opts, args = getopt.getopt(sys.argv[1:],'hk:i:m:')
except getopt.GetoptError:
    print("Usage: cbcmac-ver.py -k <keystring> -i <inputfile> -m <macfile>")
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print("Usage: cbcmac-ver.py -k <keystring> -i <inputfile> -m <macfile>")
        sys.exit()
    elif opt == '-k':
        keystring = arg
    elif opt == '-i':
        inputfile = arg
    elif opt == '-m':
        macfile = arg

if len(keystring) != 16:
    print('Error: Key string must be 16 character long.')
    sys.exit(2)

if len(inputfile) == 0:
    print('Error: Name of input file is missing.')
    sys.exit(2)

if len(macfile) == 0:
    print('Error: Name of MAC file is missing.')
    sys.exit(2)

# read the content of the MAC file into mac
ifile = open(macfile, 'rb')
mac = ifile.read()
ifile.close()

# read the content of the input file into msg
ifile = open(inputfile, 'rb')
msg = ifile.read()
ifile.close()

# pad msg if needed, padding sheme is x80 x00 ... x00
plen = AES.block_size - len(msg)%AES.block_size
if (plen != AES.block_size):
    msg += b'\x80'
    if (plen > 1):
        msg += b'\x00'*(plen-1)

# initialize all 0 iv
iv = b'\x00'*AES.block_size

# create AES cipher object
key = keystring.encode('utf-8')
cipher = AES.new(key, AES.MODE_CBC, iv)

# compute CBC MAC value
emsg = cipher.encrypt(msg)
comp_mac = emsg[-AES.block_size:]

# compare MACs
if (comp_mac == mac):
    print("Verification succeeded: valid MAC.")
else:
    print(comp_mac, mac)
    print("Verification failed: invalid MAC.")
