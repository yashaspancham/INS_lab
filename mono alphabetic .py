#A monoalphabetic cipher is a type of substitution cipher where each
# letter in the plaintext is replaced by a fixed letter
# in the ciphertext. In other words, it's a one-to-one mapping of
# letters from the plaintext to the ciphertext. Unlike the Caesar
# cipher, where each letter is shifted by a constant amount,
# monoalphabetic ciphers can use any mapping of letters.
#Example:
# Plaintext: HELLO
#Ciphertext: SVOOL
#Here key is the alphabet in reverse order(D2 did it this way)
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
key=alphabet.copy()
key.reverse()

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