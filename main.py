import math
from sympy import *

# Modular Inverse Function
def modInverse(a, m):
     
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1


# RSA keys Generation
def key_generation(p,q,e):
    if isprime(p) and isprime(q):
        global n,phi
        n = p * q
        phi = (p-1)*(q-1)

        if 1 < e and e < phi :
            global d
            d = modInverse(e,phi)

        else:
            print("e not valid")

    else:
        print("q or p not prime")
        
    
    print("\nPublic  Key : k1 = ("+str(n)+","+str(e)+")")
    print("Private Key : k2 = "+str(d))

# RSA Message Encryption
def rsa_encryption(plaintext):

    ords = []
    plain_int = ""
    for i in plaintext:
        if i.isupper():
            ords.append(str(ord(i) - 64))
        
        elif i.islower():
            ords.append(str(ord(i) - 96))

    plaintext = int(plain_int.join(ords))

    ciphertext = (plaintext ** e1) % n
    print(f'ciphertext : {ciphertext}')


# RSA Message Decryption
def rsa_decryption(ciphertext):

    plaintext = (ciphertext ** d) % n
    print(f'plaintext = {plaintext}')


# Ask For Variable
p1 = int(input('\nYou Have To Generate Your Keys In Order To Start Encryption\nEnter the value of p :'))
q1 = int(input('Enter the value of q :'))
e1 = int(input('Enter the value of e :'))

key_generation(p1,q1,e1)

while True:
    choice = input("\nChoose Your Operation's Way :\n1-Encryption\n2-Decryption\n3-Exit>>")

    if choice == "1":
        m = input("\nEnter Your String Message : ")
        rsa_encryption(m)

    elif choice == "2" :
        c = int(input("\ncEnter Your Integers Ciphertext : "))
        rsa_decryption(c)

    elif choice == "q":
        exit()

    else:
        print("Invalid Input :/")
