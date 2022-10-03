from cryptography.fernet import Fernet
from genericpath import exists
from pathlib import Path

##### Existencia del archivo .key #####
fileName = "filekey.key"
if (exists(fileName)==False):
########## Generar clave ##############
    key = Fernet.generate_key() 
    with open('filekey.key', 'wb') as filekey: 
     filekey.write(key)
########## Lectura de clave ############
with open('filekey.key', 'rb') as filekey: 
    key = filekey.read()   
fernet = Fernet(key) 

############## Encriptar ############## 
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

############## Desencriptar ###########
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
