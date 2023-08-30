from random import choice
alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def encryption():
    plain_text=input("Enter the plain text: ").lower()
    key=int(input("Enter key: "))
    cipher_text=""
    for i in plain_text:
        if i==" ":
            cipher_text+=" "
        else:
            cipher_text+=alphabets[(alphabets.index(i)+key)%26]
    return cipher_text

def decryption():
    cipher_text=input("Enter the cipher text: ").lower()
    key=int(input("Enter key: "))
    plain_text=""
    for i in cipher_text:
        if i==" ":
            plain_text+=" "
        else:
            plain_text+=alphabets[(alphabets.index(i)-key)%26]
    return plain_text

choice=int(input("Enter 1 for encryption and 2 for decryption: "))
if choice==1:
    print(encryption().upper())
elif choice==2:
    print(decryption().upper())

