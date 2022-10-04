from cryptography.fernet import Fernet
from genericpath import exists
from pathlib import Path

##### Exist file .key #####
fileName = "filekey.key"
if (exists(fileName)==False):
########## Generate key ##############
    key = Fernet.generate_key() 
    with open('filekey.key', 'wb') as filekey: 
     filekey.write(key)
########## Key reading ############
with open('filekey.key', 'rb') as filekey: 
    key = filekey.read()   
fernet = Fernet(key) 

############## Encrypt ############## 
def encriptar(archivo_encriptar):
    if (exists(archivo_encriptar)==True):
        with open(archivo_encriptar, 'rb') as file: 
            original = file.read() 
        encrypted = fernet.encrypt(original) 
        with open(archivo_encriptar, 'wb') as encrypted_file: 
            encrypted_file.write(encrypted)
        print("\nEncrypted file.\n")
    else: 
        print("The file name entered not exist.")

##############  Dencrypt ###########
def desencriptar(archivo_desencriptar):
    if (exists(archivo_desencriptar)==True):
        with open(archivo_desencriptar, 'rb') as enc_file: 
            encrypted = enc_file.read() 
        decrypted = fernet.decrypt(encrypted) 
        with open(archivo_desencriptar, 'wb') as dec_file: 
            dec_file.write(decrypted) 
        print("\nDencrypted file.\n")
    else: 
        print("The file name entered not exist.")
