# import required module
from cryptography.fernet import Fernet
import os
path = "."
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
    
fernet = Fernet(key)

with open('password.key', 'rb') as filekey:
	password = filekey.read()

skipfiles = ['encrypt.py', 'filekey.key', 'decrypt.py']

password = fernet.decrypt(password)
inputPassword = input("Password: ")

if inputPassword == password.decode('utf-8'):
    for root, d_names, f_names in os.walk(path):
        if (len(f_names)):
            for file in f_names:
                if (file in skipfiles):
                    continue
                filename = root + '\\' + file
                print(filename)
                with open(filename, 'rb') as enc_file:
                    encrypted = enc_file.read()

                decrypted = fernet.decrypt(encrypted)

                with open(filename, 'wb') as dec_file:
                    dec_file.write(decrypted)
else:
    print("Wrong password!")
