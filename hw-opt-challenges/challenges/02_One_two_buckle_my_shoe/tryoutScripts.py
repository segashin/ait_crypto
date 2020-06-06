#%%
import os
f0 = "LabProfile-v1.crypt"
f1 = "LabProfile-v1.1.crypt"

f0 = os.path.join(os.getcwd(), f0)
f1 = os.path.join(os.getcwd(), f1)
ifile0 = open(f0, "rb")
ifile1 = open(f1, "rb")

#%%
def diff():
    x = ifile0.read(16)
    y = ifile1.read(16)
    print(x)
    print(y)
    res = ""
    for i in range(len(x)):
        z = (x[i]) ^(y[i]) ^ ord(" ")
        res += chr(z)
    print(res)
    return res

def diffA(x, y):
    print(x)
    print(y)
    res = ""
    for i in range(len(x)):
        z = (x[i]) ^(y[i])
        res += chr(z)
    print(res)
    return res

def diffB(a):
    x = ifile0.read(16)
    y = ifile1.read(16)
    print(x)
    print(y)
    res = ""
    for i in range(16):
        z = (x[i]) ^(y[i]) ^ ord(a[i])
        res += chr(z)
    print(res)
    return res

# %%
wfile = open("output.txt", "w")
for i in range(50):
    wfile.write(diff())
wfile.close()

#%%

wfile1 = open("output3.txt", "w")
a = "le targeted atta"
for i in range(50):
    wfile1.write(diffB(a))
wfile1.close()

#%%
t = "veral high-profiveral high-profiveral high-profiveral high-profiveral high-profiveral high-profiveral high-profiveral high-profi7+5Sh&*!p:\"(ErxFyMc*m1RupiroslF]]r\"!/glbmf*ivl#agg,txmceqeza-8y.}bmq!fec analysis of se"
print(len(t))



#%%
chunk0 = b'5\x9c\x820\x0c`\x1e\x07>\xf5\xd447l\xee\xf7'
chunk1 = b'V\xce\xdbCU\x13\x1ek\x7f\xb7\xd84U9\xaa\xb6'
ptext_unknown = b"CrySyS Lab, Buda"
diffA(chunk0, ptext_unknown)
diffA(chunk1, ptext_unknown)

# %%
import Crypto.Cipher.AES
import Crypto.Util.Counter

#%%
keystring = ptext_unknown
ctr = Crypto.Util.Counter.new(128)
cipher = Crypto.Cipher.AES.new(chunk0, Crypto.Cipher.AES.MODE_CTR, counter=ctr)


# %%
f0 = "LabProfile-v1.crypt"
f1 = "LabProfile-v1.1.crypt"

f0 = os.path.join(os.getcwd(), f0)
f1 = os.path.join(os.getcwd(), f1)
ifile0 = open(f0, "rb")
ifile1 = open(f1, "rb")

for i in range(20):
    ptext = cipher.decrypt(ifile0.read(16))
    print(ptext.decode('ascii'))


#%%
"""

chunk0 = b'5\x9c\x820\x0c`\x1e\x07>\xf5\xd447l\xee\xf7'
chunk1 = b'V\xce\xdbCU\x13\x1ek\x7f\xb7\xd84U9\xaa\xb6'
chunk_diff = b'cRYsYs lAB \x0cbUDA'
#chunk_diff = b"cRYsYs lAB  bUDA"

def diffA():
    x = chunk0
    y = chunk_diff
    print(x)
    print(y)
    res = ""
    for i in range(len(x)):
        z = (x[i]) ^(y[i])
        res += (chr(z))
    print(res)
    return res
    
chunk_diff = diffA()
print(chunk_diff)



#%%

def diffB():
    x = chunk_diff
    y = chunk0
    print(x)
    print(y)
    res = ""
    for i in range(len(x)):
        z = (ord(x[i])) ^(y[i])
        res += chr(z)
    print(res)
    
diffB()

# %%
import Crypto.Cipher.AES
import Crypto.Util.Counter


#%%
chunk_diff = b'cRYsYs lAB \x0cbUDA'
keystring = chunk_diff
ctr = Crypto.Util.Counter.new(128)
cipher = Crypto.Cipher.AES.new(keystring, Crypto.Cipher.AES.MODE_CTR, counter=ctr)


# %%
f0 = "LabProfile-v1.crypt"
f1 = "LabProfile-v1.1.crypt"

f0 = os.path.join(os.getcwd(), f0)
f1 = os.path.join(os.getcwd(), f1)
ifile0 = open(f0, "rb")
ifile1 = open(f1, "rb")

for i in range(20):
    ptext = cipher.decrypt(ifile0.read(16))
    print(ptext.decode('ascii'))


# %%
adfs = "VÎÛCU>k·ô8U9ª¶".encode('utf-8')
f0 = "LabProfile-v1.crypt"
f1 = "LabProfile-v1.1.crypt"

f0 = os.path.join(os.getcwd(), f0)
f1 = os.path.join(os.getcwd(), f1)
ifile0 = open(f0, "rb")
ifile1 = open(f1, "rb")

def diff():
    x = ifile0.read(16)
    y = adfs
    print(x)
    print(y)
    res = ""
    for i in range(len(x)):
        z = (x[i]) ^(y[i]) ^ ord(" ")
        res += chr(z)
    print(res, len(res), len(x))
    return res



# %%
for i in range(50):
    diff()

# %%
"""