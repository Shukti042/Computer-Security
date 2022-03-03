# Advanced Encryption Standard (AES)

In this assignment you will have to implement the Advanced Encryption Standard (AES) algorithm for 128-bit key.

### Overview of AES

Advanced Encryption Standard (AES) is a popular and widely adopted symmetric key encryption algorithm.
AES uses repeat cycles or "rounds". There are 10, 12, or 14 rounds for keys of 128, 192, and 256 bits, respectively.
Each round of Algorithm consists of four steps:

1. **subBytes:** for each byte in the array, use its value as an index into a fixed 256-element lookup table, and replace its value in the state by the byte value stored at that location in the table. You can find the table and the inverse table on the web.
2. **shiftRows:** Let Ri denote the ith row in state. Shift R0 in the state left 0 bytes (i.e., no change); shift R1 left 1 byte; shift R2 left 2 bytes; shift R3 left 3 bytes. These are circular shifts. They do not affect the individual byte values themselves. Shift left for decryption.
3. **mixColumns:** for each column of the state, replace the column by its value multiplied by a fixed 4 x 4 matrix of integers (in a particular Galois Field). This is a relatively complex step, but if you utilize the BitVector library demonstrated in the sessional class it will be simple matrix multiplication. Note that the inverse operation multiplies by a different matrix.
4. **addRoundkey:** XOR the state with a 128-bit round key derived from the original key K by a recursive process.

The final round is slightly different from the others. Implementation details can be found in the presentation slide shared in the sessional class.


<p align="center">
  <img src="https://github.com/Shukti042/Computer-Security/blob/master/AES/AES%20Block%20Diagram.png" width="500" height="700" />
</p>
<p align="center">
  <u>**Figure:** **Block Diagram of AES**</u>
</p>

											



#### Task 1: Key Scheduling

The key has been provided by the user as ASCII string. If the string length was less than 16 (16x8 = 128 bit), padded it with ‘0’ and if the length was greater than 16 ignored extra characters.
Implemented the key scheduling algorithm in this step and generated keys for all the rounds.
Link of the algorithm: https://en.wikipedia.org/wiki/AES_key_schedule

#### Task 2: Encryption 

The encryption method would encrypt a block of text (128 bit/16 characters) with the keys generated in 1. I had to divide the input plain text into blocks of 16 characters and encrypt one block at a time. Padded the input string with spaces if its length was not multiple of 16.

#### Task 3: Decryption

Decrypted the encrypted text blocks and observed if they matched with the original text. Also reported the execution time. A sample output is shown below. 

Plain Text: 

Key:

BUET CSE16 Batch [In ASCII] 42554554204353453136204261746368 [In HEX] 

WillGraduateSoon [In ASCII] 57696c6c4772616475617465536f6f6e [In HEX]

Cipher Text: 54b0f718f62f03c0a455ed78007c6386 [In HEX] T°÷ö/------------------À¤Uíx􀳦|c† [In ASCII]

Deciphered Text: 57696c6c4772616475617465536f6f6e [In HEX] WillGraduateSoon [In ASCII]

Execution Time Key Scheduling: 0.01599264144897461 seconds 

Encryption Time: 0.2241218090057373 seconds 

Decryption Time: 0.3562753200531006 seconds

#### Task 4: Additional Functionalities 

1. Modified my program so that I could encrypt and decrypt not only text but also other objects (e.g., pdf, image etc.)
2. Generated the S-Box and the Inverse S-Box tables instead of using hardcoded values. I used the gf_MI()function of the BitVector module for calculating multiplicative inverse.
Ref: https://en.wikipedia.org/wiki/Rijndael_S-box
