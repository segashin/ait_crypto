#%%

#generate keys
from Crypto.PublicKey import RSA
for dst in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    with open('private_keys/'+dst+".pem", "wb") as f:
        f.write(private_key)
    with open('public_keys/'+dst+".pem", "wb") as f:
        f.write(public_key)


# %%
from Crypto.PublicKey import RSA

private_key = open("./server/private_keys/Z.pem", "rb").read()
print(private_key)


# %%
key = RSA.import_key(private_key)
encrypted_key = key.export_key(passphrase="sepfmp", pkcs=8, protection="scryptAndAES128-CBC")
with open("./server/private_keys/Z.pem", "wb") as f: f.write(encrypted_key)


#%%
import secrets
iv = secrets.token_bytes(16)
print(iv)



# %%
from Crypto.Cipher import AES, PKCS1_OAEP
import secrets
def mkpad(s, size):
    s = s.encode("utf-8")  # UTF-8文字列をバイト列に変換する
    pad = b' ' * (size - len(s) % size)  # 特定の長さの倍数にするための空白を生成
    return s + pad

iv = b'\x8c\xbcW\xcf\x0b\xa6\x00\xec\xa7\x94\xd2\x9a\x01Z\xd7\xfc'
key = "sepfmp"
key = mkpad(key, 16)
ptext = "asdf"
ptext = mkpad(ptext, 16)
cipher = AES.new(key, AES.MODE_CBC, iv)
ctext = cipher.encrypt(ptext)

#save password
with open("./server/password/A", "wb") as f: f.write(ctext)



# %%
