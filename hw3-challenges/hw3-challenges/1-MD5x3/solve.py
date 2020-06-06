from Crypto.Hash import MD5
from Crypto.Util.strxor import strxor 

class TypeError(Exception):
    def __init__(self, message):
        self.message = message

class LengthError(Exception):
    def __init__(self, message):
        self.message = message

def RF(L, R, RK):
    md5 = MD5.new()
    md5.update(RK[0:1]+R+RK[1:2])
    return strxor(L, md5.digest()), R

def ENC(X, K):

    if type(K) != bytes:
        raise TypeError("Key must be of type bytes!")
        return
    
    if len(K) != 6:
        raise LengthError("Key length must be of length 6 bytes!")
        return
    
    if type(X) != bytes:
        raise TypeError("Input block must be of type bytes!")
        return
    
    if len(X) != 32:
        raise LengthError("Block length must be of length 32 bytes!")
        return    
    
    K0 = K[0:2]
    K1 = K[2:4]
    K2 = K[4:6]
    
    L, R = X[0:16], X[16:32]
    L, R = RF(L, R, K0)
    L, R = R, L
    L, R = RF(L, R, K1)
    L, R = R, L
    L, R = RF(L, R, K2)
    Y = L + R
    
    return Y 

def DEC(Y, K):

    if type(K) != bytes:
        raise TypeError("Key must be of type bytes!")
        return
    
    if len(K) != 6:
        raise LengthError("Key length must be of length 6 bytes!")
        return
    
    if type(Y) != bytes:
        raise TypeError("Input block must be of type bytes!")
        return
    
    if len(Y) != 32:
        raise LengthError("Block length must be of length 32 bytes!")
        return    
    
    K0 = K[0:2]
    K1 = K[2:4]
    K2 = K[4:6]
    
    L, R = Y[0:16], Y[16:32]
    L, R = RF(L, R, K2)
    L, R = R, L
    L, R = RF(L, R, K1)
    L, R = R, L
    L, R = RF(L, R, K0)
    X = L + R
    
    return X 

res1 = []
res2 = []
for i in range(2**16):
    res1.append(RF(b"*THIS_IS_A_TEST_",b"INPUT_FOR_MD5X3*", i.to_bytes(2, 'big'))[0])
    res2.append(RF(0xc5723c92da1d7509cf56ae15bdc0fbdd.to_bytes(16,'big'),0x5c46a303511ed25690522cff9e62ce65.to_bytes(16,'big'), i.to_bytes(2, 'big'))[0])


key01 = 0
key23 = 0
key45 = 0

from tqdm import tqdm
for i in tqdm(range(len(res1))):
    for j in range(len(res2)):
        if res1[i] == res2[j]:
            key01 = i
            key45 = j
            print(key01, key45)
            break

dmsg = 0xc5723c92da1d7509cf56ae15bdc0fbdd5c46a303511ed25690522cff9e62ce65.to_bytes(32, 'big')
from tqdm import tqdm
for h in range(2**16):
    if(ENC(b"*THIS_IS_A_TEST_INPUT_FOR_MD5X3*", (key45+h*65536+key01*16**8).to_bytes(6,'big')) == dmsg):
        key23 = h
        break

print(key01, key23, key45)
print(hex(key01*16**8+key23*16**4+key45))

