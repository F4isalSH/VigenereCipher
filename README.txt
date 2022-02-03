## Vigenere Cipher Encryption and Decryption Tool

Rules and input needed:
-----------------------------------------------------------------------------------------
Encryption rules:
The file that you will provide will need to have the following:
-First line must be the key that will be used to encrypt
-The line(s) after it must be the message

When running the program, it will need the following as input:
-A file path (provide the file path to any file you would like to encrypt)
-----------------------------------------------------------------------------------------
Decryption rules:
The file that you will provide will need to have the following:
-The encrypted message

When running the program, it will need the following as input:
-A file path (provide the file path to any file you would like to decrypt)
-The key that was used to encrypt the file
-----------------------------------------------------------------------------------------
Example on how to use the program:
-You can either use command line to run the program or use something like VSCode to compile it, but for
 this example, we will use the command line (WINDOWS).

Open cmd and do the following:
1- cd Desktop\VigenereCipher (Path could be different depending on where you store the file)
2- python vigenereCipher.py
3- You will be provided with three options:

   Option 1:
   -This option is for encryption, you will need to provide the path to file you would like to encrypt
   -After successfully providing the correct path, a new file called 'encrypted.dec' will be created and stored in the same folder as the program
   -Encryption finished
 
   Option 2:
   -This option is for decryption, you will need to provide the path to file you would like to decrypt and you will need to provide the encryption key used
   -After successfully providing the correct path and the encryption key, a new file called 'decrypted.txt' will be created and stored in the same folder as the program
   -Decryption finished

   Option 3:
   This option will shutdown the program.

There is also a test file 'message.txt' that you can use for encryption and test out the program.
This program was coded with python so please make sure you have python installed on your system.
