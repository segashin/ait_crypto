#%%
import textbookRSA
#%%
f = open("rsapubkey.txt", "r")
e = int(f.readline())
n = int(f.readline())
f.close()

rsa = textbookRSA.TextbookRSA({'e':e, 'n':n, 'd':0})

key = rsa.getKey()
e = key['e']
n = key['n']

print("\nPublic key: ")
print(e)
print(n)

f = open("ciphertext.txt", "r")
ciphertext = int(f.read())
f.close()

print("\nCiphertext: ")
print(ciphertext)

#%%
# Compute the plaintext as the e-th root of the ciphertext. 
# Identify and use the appropriate function for computing e-th root in the textbookRSA.py module!
plaintext = textbookRSA.findInvPow(ciphertext, e)

print("\nPlaintext recovered: ")
print(plaintext)

print("\nPrinted as a string: ")
print(plaintext.to_bytes(len(format(plaintext, 'x'))//2, byteorder='big').decode('utf-8') + '\n')


