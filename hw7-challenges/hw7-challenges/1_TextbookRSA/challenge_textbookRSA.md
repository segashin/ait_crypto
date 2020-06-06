Breaking textbook RSA
=====================

In this challenge, you will see yourself that using textbook RSA without PKCS#1 OAEP padding is not secure. Given an implementation of textbook RSA in the textbookRSA.py module, an RSA public key (e, n) in rsapubkey.txt, and a ciphertext produced with textbook RSA and the public key in ciphertext.txt, your task is to break the ciphertext without knowledge of the private RSA key!

Note that in this challenge the public key and the ciphertext are represented as decimal numbers, which are saved as strings in the files.

The ciphertext seems to be a large number, but actually it is small compared to the modulus n. So you may want to exploit textbook RSA's weakness related to encrypting small messages.

We started to write the attack script break_ciphertext.py. Complete this script by figuring out how to compute the plaintext!
