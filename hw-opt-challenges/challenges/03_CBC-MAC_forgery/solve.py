#%%
#read file1
freader = open("file1.bin", 'rb')
msg1 = freader.read()
freader.close()

#read file2
freader = open("file2.bin", 'rb')
msg2 = freader.read()
freader.close()

#read mac1
freader = open("file1-mac.bin", 'rb')
mac1 = freader.read()
freader.close()

#read mac2
freader = open("file2-mac.bin", 'rb')
mac2 = freader.read()
freader.close()

#%%
from Crypto.Cipher import AES
print(len(msg1),AES.block_size)
print(len(msg2),AES.block_size)
iv = b'\x00'*AES.block_size

end_block = mac1[-AES.block_size:]
concat_str = b""
for i in range(16):
    concat_str += (end_block[i] ^ iv[i] ^ msg2[i]).to_bytes(1, 'big')
print(concat_str)
    

#write file12
fwriter = open("file12.bin", 'wb')
fwriter.write(msg1+concat_str+msg2[16:])
fwriter.close()

#%%
from Crypto.Cipher import AES
iv = b'\x00'*AES.block_size

pad_msg2 = msg2+b'\x80'+b'\x00'*7

end_block = mac2[-AES.block_size:]
concat_str = b""
for i in range(16):
    concat_str += (end_block[i] ^ iv[i] ^ msg1[i]).to_bytes(1, 'big')
print(concat_str)
 

#write file21
fwriter = open("file21.bin", 'wb')
fwriter.write(pad_msg2+concat_str+msg1[16:])
fwriter.close()

