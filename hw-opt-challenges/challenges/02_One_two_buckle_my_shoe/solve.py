import os
f0 = "LabProfile-v1.crypt"
f1 = "LabProfile-v1.1.crypt"

f0 = os.path.join(os.getcwd(), f0)
f1 = os.path.join(os.getcwd(), f1)
ifile0 = open(f0, "rb")
ifile1 = open(f1, "rb")

def diffB(a):
    x = ifile0.read(16)
    y = ifile1.read(16)
    #print(x)
    #print(y)
    res = ""
    for i in range(16):
        z = (x[i]) ^(y[i]) ^ ord(a[i])
        res += chr(z)
    print(res)
    return res


wfile3 = open("output4.txt", "w")
pfile = open("output_ptext.txt", "w")
a = "tory Was involve"
for i in range(11):
    res = diffB(a)
for i in range(100):
    res = diffB(a)
    a = res
    wfile3.write(res)

wfile3.close()

"""
wfile3 = open("output3.txt", "w")
pfile = open("output_ptext.txt", "w")
a = "veral high-profi"
for i in range(14):
    res = diffB(a)
for i in range(50):
    res = diffB(a)
    a = res
    wfile3.write(res)

wfile3.close()
"""
