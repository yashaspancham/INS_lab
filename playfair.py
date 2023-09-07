alphabet=["a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
key=input("Enter the key: ").lower()


def createMatrix(key):
    #construction of playfair matrix
    #preprocessing key
    key=key.replace(" ","")
    key=key.replace("j","i")
    new_key=""
    for i in key:
        if i not in new_key:
            new_key+=i
    key=new_key

    #initilize matrix
    matrix=[]
    for i in range(0,5):
        temp=[]
        for j in range(0,5):
            temp.append("dummy_value")
        matrix.append(temp.copy())
        temp.clear()
    #Fill Matrix with Key
    row,col=0,0
    for i in key:
        matrix[row][col]=i
        alphabet.remove(i)
        col+=1
        if col==4:
            row+=1
            col=0

    for i in range(5):
        for j in range(5):
            if(matrix[i][j]=="dummy_value"):
                matrix[i][j]=alphabet[0]
                alphabet.remove(matrix[i][j])
    return matrix

#matrix=createMatrix(key)

plaintext=input("Enter the string: ").lower()
plaintext=plaintext.replace(" ","")
temp=""
for i in range(len(plaintext)-1):
    if plaintext[i]==plaintext[i+1]:
        temp+=plaintext[i]+"x"
    else:
        temp+=plaintext[i]
temp=temp+plaintext[-1]
plaintext=temp

def encrypt(plaintext,matrix):
    ciphertext=""