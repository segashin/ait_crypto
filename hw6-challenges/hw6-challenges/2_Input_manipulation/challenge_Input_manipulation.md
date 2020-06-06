Input manipulation
==================

A program uses the following PRNG to generate cryptographic parameters (such as keys, IVs, etc.):

              X_i
               |
         +-----+
         |     |
         |     |
    T_i ----->[+]--->[ MD5 ]---+---> output_i = MD5(X_i + T_i)
         |                     |
         |                     |
         +--->[+]<-------------+
               |
               |
              X_i+1 = X_i + output_i

where
- X_i is the 16-byte internal state of the PRNG when the i-th output is generated
- T_i is some random input (e.g., disk access time, network delays, etc.) collected from the computer and used in the generation of the i-th output
- the hash function MD5 is used to generate the output, so the output is 16 bytes long
- the [+] operator denotes XOR (as usual).

Let’s assume that we have access to the computer and we can observe and manipulate the input T of the PRNG, but we don’t have access to its internal state X. We obtained the i-th output (printed as a hex string):

	0ddb92c921c373c10703d2844c5b5bf8

generated from

	T_i  =  01b25220e627317ada9e385efbd2bf27

Can we choose the next input T_i+1 such that the PRNG generates the same output again? How?

