import random
import pandas as pd 
from genericpath import exists
from werkzeug.security import generate_password_hash
from C_encrip_file import encriptar, desencriptar


minus = "abcdefghijklmnopqrstuvwxyz"
mayus = minus.upper()
numeros = "0123456789"
simbolos = "@()[]{}*,;/-_¿?.¡!$<#>&+%="
base = minus+mayus+numeros+simbolos
longitud = 12
csv=".csv"


print("\n")
print("Menu: ")
print("\n1) Create and encrypt password at random. \n2) Encrypt existing passwords. \n3) Show passwords already encrypted with the program. \n4) Encrypt previously saved file. \n5) Decrypt previously encrypted file with the program. \n6) Exit.")
op_usuario=int(input("Chouse option: "))

### Crear y encriptar contraseñas al azar ###
if (op_usuario==1):
    rpu_1=int(input("\nEnter the number of passwords you want to generate: "))
    for i in range(rpu_1):
        muestra = random.sample(base, longitud)
        if (i==0):
            password  = ["".join(muestra)]
            password_encriptado = [generate_password_hash(password[i])]

        elif(i>0):
            password.append("".join(muestra))
            password_encriptado.append(generate_password_hash(password[i]))
        cont=i+1
        print("\n")
        print("PASSWORD NUMBER {} => {} => ENCRYPT NUMBER {} => {}".format(cont, password[i], cont, password_encriptado[i]))
        print("\n")
    save_or_not=int(input("Menu: \n1) Save passwords and encrypted. \n2) Exit. \nChoose an option: "))
    if(save_or_not==1):
        ## Guardar contraseñas ##
        df_password=pd.DataFrame(password, columns=['PASSWORDS'])
        claves=str(input("\nHow you want to save passwords: "))
        claves=claves+csv
        df_password.to_csv(claves, index=False)

        ## Guardar encriptado ##
        df_encriptado=pd.DataFrame(password_encriptado, columns=['PASSWORDS ENCRYPTED'])
        encriptado=str(input("\nHow you want to save passwords encrypted: "))
        encriptado=encriptado+csv
        df_encriptado.to_csv(encriptado, index=False)

        ## Encriptar archivo contraseñas ##
        encrip_archivo=str(input("\nYou want to encrypt the password file? Yes (y) or Not (n): "))
        encrip_archivo=encrip_archivo.upper()
        while (encrip_archivo != "Y" and encrip_archivo != "YES" and encrip_archivo != "N" and encrip_archivo != "NOT"):
            encrip_archivo=str(input("\nYou want to encrypt the password file? Yes (y) or Not (n): "))
            encrip_archivo=encrip_archivo.upper()
        if (encrip_archivo=="Y" or encrip_archivo=="YES"):
            encriptar(claves)
            print("\nIf you want to decrypt the file run the program again and choose option #5\n")
        elif (encrip_archivo=="N" or encrip_archivo=="NOT"):
            print("\nThank you for choosing our services.\n")
    else:
        print("\nThank you for choosing our services.\n")

### Encriptar contraseñas ya existentes ###
elif (op_usuario==2):
    rpu_2=int(input("Enter the number of passwords you want to encrypt: "))
    for i in range(rpu_2):
        if (i==0):
            password=[str(input("Enter password to encrypted: "))]
            password_encriptado = [generate_password_hash(password[i])]
        elif (i>0):
            password.append(str(input("Enter the next password to encrypted: ")))
            password_encriptado.append(generate_password_hash(password[i]))    
        cont=i+1
        print("\n")
        print("PASSWORD NUMBER {} => {} => ENCRYPT NUMBER {} => {}".format(cont, password[i], cont, password_encriptado[i]))
        print("\n")
    save_or_not=int(input("Menu: \n1) Save passwords and encrypted. \n2) Exit. \nChoose an option: "))
    if(save_or_not==1):
        ## Save passwords ##
        df_password=pd.DataFrame(password, columns=['PASSWORDS'])
        claves=str(input("\nHow you want to save passwords: "))
        claves=claves+csv
        df_password.to_csv(claves, index=False)

        ## Save encrypted ##
        df_encriptado=pd.DataFrame(password_encriptado, columns=['PASSWORDS ENCRYPTED'])
        encriptado=str(input("\nHow you want to save passwords encrypted: "))
        encriptado=encriptado+csv
        df_encriptado.to_csv(encriptado, index=False)

        ## Encriptar archivo contraseñas ##
        encrip_archivo=str(input("\nYou want to encrypt the password file? Yes (y) or Not (n): "))
        encrip_archivo=encrip_archivo.upper()
        while (encrip_archivo != "Y" and encrip_archivo != "YES" and encrip_archivo != "N" and encrip_archivo != "NOT"):
            encrip_archivo=str(input("\nYou want to encrypt the password file? Yes (y) or Not (n): "))
            encrip_archivo=encrip_archivo.upper()
        if (encrip_archivo=="Y" or encrip_archivo=="YES"):
            encriptar(claves)
            print("\nIf you want to decrypt the file run the program again and choose option #5\n")
        elif (encrip_archivo=="N" or encrip_archivo=="NOT"):
            print("\nThank you for choosing our services.\n")
    else:
        print("\nThank you for choosing our services.\n")


### Mostrar contraseñas ya encriptadas ###
elif (op_usuario==3):
    from B_check_my_password import check
    print("\nPlease make sure that the file where the passwords are located is not encrypted.")
    print("If you are not sure, restart the program and press option #5 in the menu.")
    archivo=str(input("\nEnter the name of the file where the passwords are located: "))
    archivo=archivo+csv
    if (exists(archivo)==True):
        rpu_3=str(input("\nEnter the encrypted: "))
        rpu_3=rpu_3.replace(" ", "")
        check(archivo, rpu_3)
    else:
        print("\nThe file with name entered not exist.\n")

### Encreiptar archivo ###
elif (op_usuario==4):
    encriptar(str(input("\nEnter the file name: "))+csv)

### Desencriptar archivo ###
elif (op_usuario==5):
    desencriptar(str(input("\nEnter the file name: "))+csv)

###  Salir del programa ###
else:
    print("\nThank you for choosing our services.\n")

