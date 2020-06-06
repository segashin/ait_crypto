Bellovin's Nightmare
====================

Long time ago, Steve Bellovin and Michael Merritt designed a password based key exchange protocol that makes off-line dictionary attacks on the password infeasible. However, it needs to be implemented carefully in order for it to be really secure. In this challenge, you are given an implementation of the protocol, which consists of programs run by Alice and Bob. Luckily for you, the given implementation has a flaw that makes an off-line dictionary attack possible. Your task is to find the password shared by Alice and Bob. You have access to the implementation and messages of a recorded protocol run.

To make things a bit easier for you, we reveal that the password is a name concatenated with a 2-digit number, and the name begins with letter 'R'. A list of possible names is given in the file names.txt.

The given programs and messages are related as shown below:

+----------------+
|                |
| eke_alice_1.py |    eke_msg_1.txt    +----------------+
|                | ------------------> |                |
+----------------+                     |                |
                                       |  eke_bob_1.py  |
+----------------+    eke_msg_2.txt    |                |
|                | <------------------ |                |
|                |                     +----------------+
| eke_alice_2.py | 
|                |    eke_msg_3.txt    +----------------+
|                | ------------------> |                |
+----------------+                     |  eke_bob_2.py  |
                                       |                |
                                       +----------------+

## eke_alice_1.py

This program generates a fresh RSA key-pair and saves it locally. Then, it adds 1 to the public exponent e with probability 1/2, and encrypts the result by XORing to it a key derived from the password with the PBKDF2 key derivation function. 

The program outputs eke_msg_1.txt, which contains the salt used with PBKDF2, the encrypted exponent e, and the modulus n of the RSA public key. Note that the modulus is not encrypted. The message fields are encoded in base64 and they are separated by "new line" characters. 

## eke_bob_1.py

This program reads in eke_msg_1.txt and tries to decrypt the encrypted exponent e with a key derived from the password and the salt with PBKDF2. If the result is even, then e is decreased by 1. Then a fresh session key is generated randomly and it is encrypted with the RSA public key (e, n). 

The program outputs eke_msg_2.txt, which conatins the encrypted session key in base64 encoding. The session key is also saved locally for future use by Bob.

## eke_alice_2.py

This program reads in eke_msg_2.txt and the previously generated RSA key-pair, and it decrypts the encrypted session key obtained from eke_msg_2.txt with the RSA private key. Then, the program takes some user input from the keyboard and it encrypts that with the session key using AES in CTR mode.

The program outputs eke_msg_3.txt, which contains the nonce used with AES-CTR and the encrypted user input. The message fields are encoded in base64 and separated by "new line" characters.

## eke_bob_2.py

Finally, this program reads in eke_msg_3.txt and the locally saved session key, and it decrypts the message and prints its content on the screen.

## Note

If you want to try these programs, you can do so, but make a copy of the files eke_msg_x.txt (x = 1, 2, 3) before doing that, because you may overwrite them when you are playing with the programs.
