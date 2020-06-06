#%%
import sys, getopt
from Crypto.Cipher import AES
from Crypto.Hash import SHA256, HMAC
from Crypto import Random
from Crypto.Hash import MD5
from Crypto.Util.strxor import strxor
from tqdm import tqdm
from datetime import datetime
from datetime import timedelta

def gen_prn(time):
    statefile = "prngstate.txt"
    prnginput = time

    # read the content of the state file
    ifile = open(statefile, 'r')
    line = ifile.readline()
    prngstate = bytes.fromhex(line[len("prngstate: "):len("prngstate: ")+32])
    ifile.close()

    # compute output and next state
    H = MD5.new()
    H.update(strxor(prnginput, prngstate))
    prngoutput1 = H.digest()
    prngstate = strxor(prngstate, prngoutput1)


    # save state
    #ofile = open(statefile, 'w')
    #ofile.write("prngstate: " + prngstate.hex())
    #ofile.close()

    #print output
    #print(prngoutput1.hex())
    #print(prngoutput2.hex())

    #return prngoutput1.hex(), 0 #prngoutput2
    return prngoutput1, prngstate

def read_message(inputfile):
    # read the content of the input file into msg
    ifile = open(inputfile, 'rb')
    msg = ifile.read()
    ifile.close()

    # parse the message
    header_length = 9                                          # header is 9 bytes long
    header = msg[0:header_length]
    iv = msg[header_length:header_length+AES.block_size]       # iv is AES.block_size bytes long
    mac_length = 32                                            # SHA256 hash is 32 bytes long
    encrypted = msg[header_length+AES.block_size:-mac_length]  # encrypted part is between iv and mac
    mac = msg[-mac_length:]                                    # last mac_length bytes form the mac
    header_version = header[0:2]        # version is encoded on 2 bytes 
    header_type = header[2:3]           # type is encoded on 1 byte 
    header_length = header[3:5]         # msg length is encoded on 2 bytes 
    header_sqn = header[5:9]            # msg sqn is encoded on 4 bytes 


    print("Message header:")
    print("   - protocol version: " + header_version.hex() + " (" + str(header_version[0]) + "." + str(header_version[1]) + ")")
    print("   - message type: " + header_type.hex() + " (" + str(int.from_bytes(header_type, byteorder='big')) + ")")
    print("   - message length: " + header_length.hex() + " (" + str(int.from_bytes(header_length, byteorder='big')) + ")")
    print("   - message sequence number: " + header_sqn.hex() + " (" + str(int.from_bytes(header_sqn, byteorder='big')) + ")")
    print("   - iv: ", iv)

    return encrypted, mac, header, iv

#%%
def formatTime(now):
    year = str(now.year)
    month = "0"+str(now.month) if len(str(now.month))==1 else str(now.month)
    day = "0"+str(now.day) if len(str(now.day))==1 else str(now.day)
    hour = "0"+str(now.hour) if len(str(now.hour))==1 else str(now.hour)
    minute = "0"+str(now.minute) if len(str(now.minute))==1 else str(now.minute)
    second = "0"+str(now.second) if len(str(now.second))<2 else str(now.second)
    msecond =  ("0" + str(now.microsecond)) if (now.microsecond)<99999 else str(now.microsecond)
    msecond = msecond[0]+ msecond[1]
    #print(year+month+day+hour+minute+second+msecond[:2])
    return(year+month+day+hour+minute+second+msecond)

def findTime():
    encrypted, mac, header, iv = read_message("message.bin")

    #observed_time = 2017030623420000
    observed_time = datetime(year=2017, month=3, day=6, hour=23, minute=42, second=00, microsecond=0)
    td = timedelta(milliseconds=10)

    for i in tqdm(range(10000000)):
        now = observed_time+td*i
        nowstr = formatTime(now)
        prn1, prn2 = gen_prn(nowstr.encode('ascii'))
        # verify the mac
        #MAC = HMAC.new(bytes.fromhex(prn1), digestmod=SHA256)
        MAC = HMAC.new(prn1, digestmod=SHA256)
        MAC.update(header)
        MAC.update(iv)
        MAC.update(encrypted)
        comp_mac = MAC.digest()

        if (comp_mac == mac):
            print("MAC mataches")
            print("MAC: " , comp_mac)
            print("time: ", observed_time+td*i)
            print("prn1: ", prn1)
            print("prngstate: ", prn2)
            return prn1, prn2

findTime()

# %%
def gen_enc_key(prnginput, prngstate):
    H = MD5.new()
    H.update(strxor(prnginput, prngstate))
    prngoutput = H.digest()
    return prngoutput


def decrypt():
    #mac key
    prn1 = b'\xd1,v\xdb2s\x8c\xf5\xbb\xcd\x7fm\xd3(}?'
    prngstate = b'dzY)l\x15j\xf7Q)\xa4\xbb\xc8\x05#\xb4'

    encrypted, mac, header, iv = read_message("message.bin")

    #2017-03-06 23:41:47.440000
    observed_time = datetime(year=2017, month=3, day=6, hour=23, minute=42, second=12, microsecond=560000)
    td = timedelta(milliseconds=10)
    for i in tqdm(range(10000000)):
        now = observed_time+td*i
        nowstr = formatTime(now)
        enckey = gen_enc_key(nowstr.encode('ascii'), prngstate)
        ENC = AES.new(enckey, AES.MODE_CBC, iv)
        decrypted = ENC.decrypt(encrypted)
        j = -1
        while (decrypted[j] == 0): j -= 1
        padding = decrypted[j:]
        decrypted = decrypted[:j]
        try:
            print()
            print(decrypted.decode('ascii'))
            print("decryption succeeded")
            return
        except:
            pass
decrypt()



# %%
