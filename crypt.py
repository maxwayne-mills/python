#!/usr/bin/env python3

import sys
import pyAesCrypt

buffersize = 64 * 1024
password = "foobar"

#file = sys.argv[1]
#print(file)

# encrypt
def encrypt(file):
    print("Encrypting file: " + file)
    pyAesCrypt.encryptFile(file, "test_data.aes", password, buffersize)

def decrypt():
    pyAesCrypt.decryptFile("test_data.txt", "test_data.aes", password, buffersize)

if int(len(sys.argv)) == 1:
    print(sys.argv[0] + " options: encrypt | decrypt")
elif sys.argv[1] == "encrypt":
    file = sys.argv[2]
    encrypt(file)
elif sys.argv[1] == "decrypt":
    file = sys.argv[2]
    decrypt(file)


