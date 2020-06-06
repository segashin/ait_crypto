
#%%
import os
mac_f = open(os.path.join(os.getcwd(),"t-mac.bin"), "rb")
tmac = mac_f.read()
print(tmac.hex())


# %%
t_f = open(os.path.join(os.getcwd(), "t.txt"), "rb")
tmsg = t_f.read()
print(tmsg)

# %%
def computeXor(bmsg):
    bmsg1 = bmsg[0:16]
    bmsg2 = bmsg[16:32]
    bmsg3 = bmsg[32:48]
    #print(bmsg1)
    #print(bmsg2)
    #print(bmsg3)
    bmsg1 = int.from_bytes(bmsg1, byteorder='big')
    bmsg2 = int.from_bytes(bmsg2, byteorder='big')
    bmsg3 = int.from_bytes(bmsg3, byteorder='big')
    #bmsg1 = int(msg1.hex(), base=16)
    #bmsg2 = int(msg2.hex(), base=16)
    #bmsg3 = int(msg3.hex(), base=16)
    #print(bmsg1)
    #print(bmsg2)
    #print(bmsg3)
    bmsgxor = bmsg1^bmsg2^bmsg3
    print(bmsgxor)


# %%
computeXor(tmsg)


# %%
fmsg1 = b"2020:02:27|11:23"
fmsg2 = b":38|21450|A74635"
fmsg3 = b"|B29846|04002500"
fmsg = fmsg1+fmsg2+fmsg3
print(fmsg)
computeXor(fmsg)

##3 = 00110011
##0 = 00110000
##x = 00000011

##7 = 00110111
##4 = 00110100

# %%
from Crypto.Util.strxor import strxor

msg1 = b'2020:02:23|11:23:38|21450|A74635|B29846|00002500'
msg2 = b'.......PUT YOUR FAKE TRANSACTION HERE...........'
msg2 = fmsg
# compute checksum
def xor_checksum(msg):
    chksum = b'\x00'*16
    for i in range(len(msg)//16):
        chksum = strxor(chksum, msg[i*16:(i+1)*16])
    return chksum

print(xor_checksum(msg1) == xor_checksum(msg2))

# %%
