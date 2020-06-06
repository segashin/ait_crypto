

###############Challenge 1

#%%
with open("ciphertext.crypt", "rb") as f:
    iv = f.read(16)
print(iv)

# %%
x_i2_iv = bytes.fromhex("9d6f86e273de3f3905bc068defea0571")
x_i0_key = bytes.fromhex("b5562ff25e66e602eae4dbd61b2d5e8b")

#x_i1 = int.from_bytes(iv, byteorder='big')^int.from_bytes(x_i2_iv, byteorder='big')
#%%
def xor_bytes(x,y):
    res = b''
    for i in range(len(x)):
        res += (x[i]^y[i]).to_bytes(1,'big')
    return res

# %%
x_i1 =  xor_bytes(iv, x_i2_iv)
key = xor_bytes(x_i0_key, x_i1)
print(key.hex())

with open('key.txt', "w") as f:
    f.write(str(key))
    


####################Challenge 2
# %%
T_i = bytes.fromhex("01b25220e627317ada9e385efbd2bf27")
O_i = bytes.fromhex("0ddb92c921c373c10703d2844c5b5bf8")




