Fake Transactions
=================

## Description

A bank is using the following format for encoding records of electronic transactions:

	| Bytes  | Fields                                        |
	|--------|-----------------------------------------------|
	| 0..3   | Transaction number (monotonically increasing) |
	| 4	     | Separator ’|’                                 |
	| 5..10	 | Source account ID                             |
	| 11     | Separator ’|’                                 |
	| 12..17 | Destination account ID                        |
	| 18	 | Separator ’|’                                 |
	| 19..25 | Amount                                        |

All fields are encoded as ASCII text. The following is an example transaction record:

	0023|A74635|B29846|0001250

where 0023 is the transaction number, A74635 is the source account ID, B29846 is the destination account ID, and the amount transferred is 1250 dollars.

You obtained 3 encrypted transaction records (printed in hex encoding):
	dc75d21cae71a1fbba62ec52ee48ac8f667eea75941d3b78f2bc
	dc75d218ae73a7fdb464e052e848ac816673ea75941d3a7df7bc
	dc75d11eae72a4f6b465ef52e94aa9836572ea75941d3b79f4bc

All these encrypted records were produced by using a stream cipher with the same key (so the same key stream were XORed to the plaintext records in all three cases).  You also managed to learn that the 3 records contain only the following 5 account IDs (but you don’t know which ID appears in which transaction and in which field):
- A74635
- B29846
- C12859
- D37465
- E12654

You also have an account in this bank, and your account ID is XXXXXX. Can you forge a valid transaction record and arrange that a large sum is transferred to your account? For this, you need to generate a valid encrypted record where:
- the transaction number is larger than any of the transaction numbers in the records you have
- the source account ID is a valid and existing account ID
- the destination account ID is XXXXXX
- the transaction value is a large sum.

## Tools

For this challenge, you will need a XOR calculator. An online one is available at [http://xor.pw](http://xor.pw)
