def encryption():
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',',','.','?','!',' ']
    encryption='';
    count = 0;
    fileName = input('Please enter the file path: ');
    with open(fileName,'r') as f:
        key = f.readline().strip('\n')
        message = f.read().replace('\n','*')

    for i in message:
        if(i != '*'):
            p = alphabet.index(i);
            k = alphabet.index(key[count%len(key)]);
            encryption += alphabet[(p+k)%67];
            count+=1;
        else:
            encryption += '\n';
        
    
    with open('encrypted.dec','w') as f:
        f.write(encryption);
    
    print('\nEncryption Successful\n');



def decryption():
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',',','.','?','!',' ']
    fileName = input('Please enter the file path: ');
    key = input('Please enter the key used to encrypt this file: ');
    with open(fileName,'r') as f:
        message = f.read().replace('\n','*')
    decryption='';
    count = 0;
    for i in message:
        if(i != '*'):
            p = alphabet.index(i);
            k = alphabet.index(key[count%len(key)]);
            decryption += alphabet[(p-k)%67];
            count+=1;
        else:
            decryption += '\n';
        
    
    decryptionKey='';
    for i in key:
        k = alphabet.index(i);
        decryptionKey += alphabet[(67-k)%67];

    with open('decrypted.txt','w') as f:
        f.write(decryptionKey+'\n'+decryption);
    
    print('\nDecryption Successful\n');




print('Welcome to the Vigenere Cipher Encryption/Decryption Tool')

while True:
    action = input('Choose an action:\n1: Encrypt a file\n2: Decrypt a file\n3: Quit program\n');
    if action == '1' :
        encryption();
    elif  action == '2' :
        decryption();
    elif  action == '3' :
        print('Program will now close.....')
        break;














