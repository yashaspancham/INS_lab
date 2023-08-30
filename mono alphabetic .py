alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
key=alphabet.copy()
key.reverse()#this is the method D2 used

def enryption():
    plainText=input("Enter the plain text: ").lower()
    cipherText=""
    for letter in plainText:
        if letter in alphabet:
            cipherText+=key[alphabet.index(letter)]
        else:
            cipherText+=letter
    return cipherText



def decryption():
    cipherText=input("Enter the cipher text: ").lower()
    plainText=""
    for letter in cipherText:
        if letter in key:
            plainText+=alphabet[key.index(letter)]
        else:
            plainText+=letter
    return plainText

choice=int(input("Enter 1 to encrypt and 2 to decrypt: "))
if choice==1:
    cipherText=enryption()
    print(f"The cipher text is: {cipherText}")
else:
    plainText=decryption()
    print(f"The plain text is: {plainText}")