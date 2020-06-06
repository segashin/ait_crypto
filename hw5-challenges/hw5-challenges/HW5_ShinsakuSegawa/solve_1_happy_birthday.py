#%%
from Crypto.Hash import MD5

def trhash(x):
    h = MD5.new()
    h.update(x)
    return h.digest()[0:4]

#%%
ss = {}
tt = {}
count = 0

s = "Dear Mr. Jones, I'm delighted to inform you that you have been selected as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you have been selected as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1


s = "Dear Mr. Jones, I'm delighted to inform you that you've been selected as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. Unfortunately, this means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you've been selected as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I'm delighted to inform you that you have been selected as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. This, unfortunately means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you have been selected as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. This, unfortunately means that you can'nt reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you've been selected as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. Unfortunately, this means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

####2
s = "Dear Mr. Jones, I'm delighted to inform you that you have been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you have been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1


s = "Dear Mr. Jones, I'm delighted to inform you that you've been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. Unfortunately, this means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you've been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I'm delighted to inform you that you have been nominated as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. This, unfortunately means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you have been nominated as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. This, unfortunately means that you can'nt reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you've been nominated as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. Unfortunately, this means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1



####3
s = "Dear Mr. Jones, I'm delighted to inform you that you have been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which will be transferred to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you have been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which will be transferred to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"

ss[count] = s;
tt[count] = t;
count+=1


s = "Dear Mr. Jones, I'm delighted to inform you that you've been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which will be transferred to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. Unfortunately, this means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you've been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will be transferred to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I'm delighted to inform you that you have been nominated as one of the winners of our competition. Your prize will be 1 million USD, which we will be transferred to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you have been nominated as one of the winners of our competition. Your prize will be 1 million USD, which we will be transferred to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you can'nt reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you've been nominated as one of the winners of our competition. Your prize will be 1 million USD, which we will be transferred to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. Unfortunately, this means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1


####4
s = "Dear Mr. Jones, I'm delighted to let you know that you have been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to let you know that you have been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1


s = "Dear Mr. Jones, I'm delighted to let you know that you've been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. Unfortunately, this means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to let you know that you've been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I'm delighted to let you know that you have been nominated as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to let you know that you have been nominated as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you can'nt reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to let you know that you've been nominated as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. Unfortunately, this means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

####5
s = "Dear Mr. Jones, I'm delighted to let you know that you have been chosen as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to let you know that you have been chosen as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1


s = "Dear Mr. Jones, I'm delighted to let you know that you've been chosen as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. Unfortunately, this means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to let you know that you've been chosen as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I'm delighted to let you know that you have been chosen as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. This, unfortunately means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to let you know that you have been chosen as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. This, unfortunately means that you can'nt reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to let you know that you've been chosen as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. Unfortunately, this means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

##########################################33
s = "Dear Mr. Jones, I'm happy to inform you that you have been selected as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you have been selected as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1


s = "Dear Mr. Jones, I'm happy to inform you that you've been selected as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. Unfortunately, this means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you've been selected as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I'm happy to inform you that you have been selected as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. This, unfortunately means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you have been selected as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. This, unfortunately means that you can'nt reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you've been selected as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. Unfortunately, this means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

####2
s = "Dear Mr. Jones, I'm happy to inform you that you have been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you have been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1


s = "Dear Mr. Jones, I'm happy to inform you that you've been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. Unfortunately, this means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you've been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I'm happy to inform you that you have been nominated as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. This, unfortunately means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you have been nominated as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. This, unfortunately means that you can'nt reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you've been nominated as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. Unfortunately, this means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1



####3
s = "Dear Mr. Jones, I'm happy to inform you that you have been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which will be transferred to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you have been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which will be transferred to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"

ss[count] = s;
tt[count] = t;
count+=1


s = "Dear Mr. Jones, I'm happy to inform you that you've been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which will be transferred to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. Unfortunately, this means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you've been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will be transferred to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I'm happy to inform you that you have been nominated as one of the winners of our competition this year. Your prize will be 1 million USD, which we will be transferred to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you have been nominated as one of the winners of our competition this year. Your prize will be 1 million USD, which we will be transferred to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you can'nt reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you've been nominated as one of the winners of our competition this year. Your prize will be 1 million USD, which we will be transferred to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. Unfortunately, this means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1


####4
s = "Dear Mr. Jones, I'm happy to let you know that you have been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to let you know that you have been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1


s = "Dear Mr. Jones, I'm happy to let you know that you've been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. Unfortunately, this means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to let you know that you've been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I'm happy to let you know that you have been nominated as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to let you know that you have been nominated as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you can'nt reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to let you know that you've been nominated as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. Unfortunately, this means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

####5
s = "Dear Mr. Jones, I'm happy to let you know that you have been chosen as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to let you know that you have been chosen as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1


s = "Dear Mr. Jones, I'm happy to let you know that you've been chosen as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. Unfortunately, this means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to let you know that you've been chosen as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I'm happy to let you know that you have been chosen as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. This, unfortunately means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to let you know that you have been chosen as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. This, unfortunately means that you can'nt reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to let you know that you've been chosen as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account within one week. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. Unfortunately, this means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1



############################################################################
s = "Dear Mr. Jones, I'm delighted to inform you that you have been selected as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you have been selected as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1


s = "Dear Mr. Jones, I'm delighted to inform you that you've been selected as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. Unfortunately, this means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you've been selected as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I'm delighted to inform you that you have been selected as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. This, unfortunately means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you have been selected as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. This, unfortunately means that you can'nt reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you've been selected as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your complaint was not approved by our management. Unfortunately, this means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

####2
s = "Dear Mr. Jones, I'm delighted to inform you that you have been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you have been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1


s = "Dear Mr. Jones, I'm delighted to inform you that you've been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. Unfortunately, this means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you've been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I'm delighted to inform you that you have been nominated as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. This, unfortunately means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you have been nominated as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. This, unfortunately means that you can'nt reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you've been nominated as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your complaint was not approved by our management. Unfortunately, this means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1



####3
s = "Dear Mr. Jones, I'm delighted to inform you that you have been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which will be transferred to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you have been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which will be transferred to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"

ss[count] = s;
tt[count] = t;
count+=1


s = "Dear Mr. Jones, I'm delighted to inform you that you've been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which will be transferred to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. Unfortunately, this means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you've been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will be transferred to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I'm delighted to inform you that you have been nominated as one of the winners of our competition. Your prize will be 1 million USD, which we will be transferred to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you have been nominated as one of the winners of our competition. Your prize will be 1 million USD, which we will be transferred to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you can'nt reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to inform you that you've been nominated as one of the winners of our competition. Your prize will be 1 million USD, which we will be transferred to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. Unfortunately, this means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1


####4
s = "Dear Mr. Jones, I'm delighted to let you know that you have been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to let you know that you have been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1


s = "Dear Mr. Jones, I'm delighted to let you know that you've been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. Unfortunately, this means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to let you know that you've been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I'm delighted to let you know that you have been nominated as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to let you know that you have been nominated as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. This, unfortunately means that you can'nt reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to let you know that you've been nominated as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was not approved by our management. Unfortunately, this means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

####5
s = "Dear Mr. Jones, I'm delighted to let you know that you have been chosen as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to let you know that you have been chosen as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1


s = "Dear Mr. Jones, I'm delighted to let you know that you've been chosen as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. Unfortunately, this means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to let you know that you've been chosen as one of the winners of our competition. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I'm delighted to let you know that you have been chosen as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. This, unfortunately means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to let you know that you have been chosen as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. This, unfortunately means that you can'nt reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am delighted to let you know that you've been chosen as one of the winners of our competition. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your complaint was rejected by our management. Unfortunately, this means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

#########################################33
s = "Dear Mr. Jones, I'm happy to inform you that you have been selected as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your claim was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you have been selected as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your claim was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1


s = "Dear Mr. Jones, I'm happy to inform you that you've been selected as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your claim was not approved by our management. Unfortunately, this means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you've been selected as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your claim was not approved by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I'm happy to inform you that you have been selected as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your claim was not approved by our management. This, unfortunately means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you have been selected as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your claim was not approved by our management. This, unfortunately means that you can'nt reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you've been selected as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I regret to inform you that your claim was not approved by our management. Unfortunately, this means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

####2
s = "Dear Mr. Jones, I'm happy to inform you that you have been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your claim was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you have been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your claim was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1


s = "Dear Mr. Jones, I'm happy to inform you that you've been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your claim was not approved by our management. Unfortunately, this means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you've been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your claim was not approved by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I'm happy to inform you that you have been nominated as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your claim was not approved by our management. This, unfortunately means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you have been nominated as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your claim was not approved by our management. This, unfortunately means that you can'nt reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you've been nominated as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to inform you that your claim was not approved by our management. Unfortunately, this means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1



####3
s = "Dear Mr. Jones, I'm happy to inform you that you have been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which will be transferred to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you have been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which will be transferred to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"

ss[count] = s;
tt[count] = t;
count+=1


s = "Dear Mr. Jones, I'm happy to inform you that you've been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which will be transferred to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was not approved by our management. Unfortunately, this means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you've been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will be transferred to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was not approved by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I'm happy to inform you that you have been nominated as one of the winners of our competition this year. Your prize will be 1 million USD, which we will be transferred to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was not approved by our management. This, unfortunately means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you have been nominated as one of the winners of our competition this year. Your prize will be 1 million USD, which we will be transferred to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was not approved by our management. This, unfortunately means that you can'nt reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to inform you that you've been nominated as one of the winners of our competition this year. Your prize will be 1 million USD, which we will be transferred to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was not approved by our management. Unfortunately, this means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1


####4
s = "Dear Mr. Jones, I'm happy to let you know that you have been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to let you know that you have been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was not approved by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1


s = "Dear Mr. Jones, I'm happy to let you know that you've been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was not approved by our management. Unfortunately, this means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to let you know that you've been nominated as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was not approved by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I'm happy to let you know that you have been nominated as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was not approved by our management. This, unfortunately means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to let you know that you have been nominated as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was not approved by our management. This, unfortunately means that you can'nt reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to let you know that you've been nominated as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was not approved by our management. Unfortunately, this means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

####5
s = "Dear Mr. Jones, I'm happy to let you know that you have been chosen as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was rejected by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to let you know that you have been chosen as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was rejected by our management. This, unfortunately means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1


s = "Dear Mr. Jones, I'm happy to let you know that you've been chosen as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was rejected by our management. Unfortunately, this means that you cannot reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to let you know that you've been chosen as one of the winners of our competition this year. Your prize will be 1,000,000 USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was rejected by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I'm happy to let you know that you have been chosen as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was rejected by our management. This, unfortunately means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to let you know that you have been chosen as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was rejected by our management. This, unfortunately means that you can'nt reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1

s = "Dear Mr. Jones, I am happy to let you know that you've been chosen as one of the winners of our competition this year. Your prize will be 1 million USD, which we will transfer to your bank account whithin seven days. Best regards, Andrew B. Clark"
t = "Dear Mr. Jones, I am sorry to let you know that your claim was rejected by our management. Unfortunately, this means that you can't reclaim your cost of 1,234 USD and in addition you have to cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
ss[count] = s;
tt[count] = t;
count+=1



# %%

sshash = {}
tthash = {}


for i in range(len(ss)):
    sshash[i] = trhash(ss[i].encode('ascii'))
    for j in range(1,1000):
        #print(ss[i][:15]+" "*j+ss[i][15:])
        sshash[str(i)+"_"+str(j)]=[trhash((ss[i][:15]+" "*j+ss[i][15:]).encode('ascii')),(ss[i][:15]+" "*j+ss[i][15:])]
for i in range(len(tt)):
    tthash[trhash(tt[i].encode('ascii'))] = i
    for j in range(1, 1000):
        tthash[trhash((tt[i][:15]+" "*j+tt[i][15:]).encode('ascii'))] = (tt[i][:15]+" "*j+tt[i][15:])

#print("sshash")
#for i in sshash:
#    print(sshash[i])
#print("tthash")
#for i in tthash:
#    print(i)

#%%
print("look for collision")
for i in sshash:
    if sshash[i][0] in tthash:
        print("hash: " , sshash[i][0])
        print("s: ", sshash[i][1])
        print("h: ", tthash[sshash[i][0]])
        break

print("finished")



# %%
#a = "Dear Mr. Jones,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    I'm delighted to inform you that you have been nominated as one of the winners of our competition. Your prize will be 1,000,000 USD, which will be transferred to your bank account within one week. Best regards, Andrew B. Clark"
#b = "Dear Mr. Jones,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              I regret to inform you that your complaint was not approved by our management. Unfortunately, means that you cannot reclaim your cost of 1,234 USD and in addition you must cover our investigation cost of 345 USD as well. Yours sincerely, Andrew B. Clark"
#print(trhash(a.encode('ascii')))
#print(trhash(b.encode('ascii')))

# %%
