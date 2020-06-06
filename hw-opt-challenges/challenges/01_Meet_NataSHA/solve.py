
#%%
import natasha

#hex string
ctext = "ae055b48d8fa60bc337ff846ee88fe33c7e026a5ea54dbb59814c68265540cef1c183ef746553686"
ptext = 'Meet_NataSHA_which_is_not_a_SHA_although'


ctextbyte = bytes.fromhex(ctext)
ptextbyte = ptext.encode("ascii")
print(ctextbyte)
print(ptextbyte)

def head(X, K):
    L, R = X[0:20], X[20:40]
    K0 = K[0:1]
    K1 = K[1:2]
    K2 = K[2:3]

    R, L = natasha.RF(L, R, K0)
    R, L = natasha.RF(L, R, K1)
    L, R = natasha.RF(L, R, K2)

    return L,R

def tail(X, K):
    L, R = X[0:20], X[20:40]
    K3 = K[0:1]
    K4 = K[1:2]
    K5 = K[2:3]

    R, L = natasha.RF(L, R, K5)
    R, L = natasha.RF(L, R, K4)
    L, R = natasha.RF(L, R, K3)

    return L, R

# %%
from tqdm import tqdm
def meet():
    resHR = []
    resHL = []
    resTR = {}
    resTL = {}
    for i in tqdm(range(2**24)):
        key = i.to_bytes(3, 'big')
        HL, HR = head(ptextbyte, key)
        TL, TR = tail(ctextbyte, key)
        resHL.append(HL)
        resHR.append(HR)
        resTL[TL] = i
        resTR[TR] = i
    return resHL, resTL, resHR, resTR

resHL, resTL, resHR, resTR = meet()


#%%
print(len(resHL))
print(len(resHR))
print(len(resTR.keys()))
print(len(resTL.keys()))

#%%

def checkCollision(res1, res2):
    for i in (range(len(res1))):
        if res1[i] in res2:
            print(res1[i])
            print(i, res2[res1[i]])
            return i, res2[res1[i]]
    return 0, 0


key1, key2 = checkCollision(resHR, resTR)
print(key1, key2)
key1, key2 = checkCollision(resHR, resTL)
print(key1, key2)
key1, key2 = checkCollision(resHL, resTR)
print(key1, key2)
key1, key2 = checkCollision(resHL, resTL)
print(key1, key2)

# %%
def checkCollisionX(res1, res2):
    print(len(res1))
    for i in res2.keys():
        if i in res1:
            print(i)
            return
    print("none")

checkCollisionX(resTR, resTL)

#%%
key0 = 3928320 
key1 = 4083196
key2 = 3928526
key3 = 16731644
"""
3928320 4083196
b'@\x05\xef\xfa\x8d\x17h\xa8\xf0\xbf\xab\xcf\x16|\xed.W\xba\xc1\x89'
3928526 16731644
3928526 16731644
"""

b0 = key0.to_bytes(3, 'big')
b1 = key1.to_bytes(3, 'big')
b2 = key2.to_bytes(3, 'big')
b3 = key3.to_bytes(3, 'big')
recovered_key = b0+b1
print(b0, b1, b2, b3)
print(recovered_key)


# %%
bp = natasha.ENC(ptextbyte, b1+b1)
print(bp)
bp = natasha.ENC(ptextbyte, b1+b2)
print(bp)
bp = natasha.ENC(ptextbyte, b1+b3)
print(bp)
bp = natasha.ENC(ptextbyte, b2+b1)
print(bp)
bp = natasha.ENC(ptextbyte, b2+b0)
print(bp)
bp = natasha.ENC(ptextbyte, b3+b1)
print(bp)
bp = natasha.ENC(ptextbyte, b3+b0)
print(bp)
print(ctextbyte)


# %%
k = b2+b1

bp = natasha.DEC(ctextbyte, k)
print("check key:  decoded=", bp.decode('ascii'))

#%%
target_ctext = bytes.fromhex("8c4febe7e2f0a6d43110d37576535b8518eaa4b7ce3ac3722816062755aa8b5ed82eadf76e8af6f5")
target_ptext = natasha.DEC(target_ctext , k)
print(target_ptext)
print("Decrypted plain text: ", target_ptext.decode('ascii'))

print("Recovered key: ", k)


# %%
