# import required module
from cryptography.fernet import Fernet
import os
import shutil
path = "."
with open('key/filekey.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)

skipfiles = ['encrypt.py', 'decrypt.py']

inputKey = input("Enter key: ")

if inputKey == key.decode('utf-8'):
    for root, d_names, f_names in os.walk(path):
        if (root == ".\key"):
            continue
        if (len(f_names)):
            for file in f_names:
                if (file in skipfiles):
                    continue
                filename = root + '\\' + file
                with open(filename, 'rb') as enc_file:
                    encrypted = enc_file.read()

                decrypted = fernet.decrypt(encrypted)

                with open(filename, 'wb') as dec_file:
                    dec_file.write(decrypted)
    for root, dirs, files in os.walk("key/", topdown=False):
        for name in files:
            os.remove(root + name)

    os.rmdir('key')
else:
    print("Wrong key!")

