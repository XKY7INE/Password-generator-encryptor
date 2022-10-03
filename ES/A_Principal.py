import random
import pandas as pd 
from genericpath import exists
from werkzeug.security import generate_password_hash
from C_encrip_archivo import encriptar, desencriptar

minus = "abcdefghijklmnopqrstuvwxyz"
mayus = minus.upper()
numeros = "0123456789"
simbolos = "@()[]{}*,;/-_¿?.¡!$<#>&+%="
base = minus+mayus+numeros+simbolos
longitud = 12
csv=".csv"


print("\n")
print("Seleccione la opción que desee: ")
print("\n1) Crear y enciptar contraseña al azar. \n2) Encriptar contraseñas ya existentes. \n3) Mostrar contraseñas ya encriptadas con el programa. \n4) Encriptar archivo guardado anteriormente. \n5) Desencriptar archivo encriptado anteriormente con el programa. \n6) Salir")
op_usuario=int(input("Dijite el numero de opción: "))

### Crear y encriptar contraseñas al azar ###
if (op_usuario==1):
    rpu_1=int(input("\nIngrese el numero de contraseñas que desea generar: "))
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
        print("CONTRASEÑA NUMERO {} => {} => ENCRIPTADO NUMERO {} => {}".format(cont, password[i], cont, password_encriptado[i]))
        print("\n")
    save_or_not=int(input("Menu \n1) Guardar las contraseñas y encriptado. \n2) Salir. \nElegir una opción: "))
    if(save_or_not==1):
        ## Guardar contraseñas ##
        df_password=pd.DataFrame(password, columns=['CONTRASEÑAS'])
        claves=str(input("\nComo desea guardar las contraseñas: "))
        claves=claves+csv
        df_password.to_csv(claves, index=False)

        ## Guardar encriptado ##
        df_encriptado=pd.DataFrame(password_encriptado, columns=['CONTRASEÑAS ENCRIPTADAS'])
        encriptado=str(input("\nComo desea guardar las contraseñas encriptadas: "))
        encriptado=encriptado+csv
        df_encriptado.to_csv(encriptado, index=False)

        ## Encriptar archivo contraseñas ##
        encrip_archivo=str(input("\nDesea encriptar el archivo de las contraseñas? Si (s) o No (n): "))
        encrip_archivo=encrip_archivo.upper()
        while (encrip_archivo != "S" and encrip_archivo != "SI" and encrip_archivo != "N" and encrip_archivo != "NO"):
            encrip_archivo=str(input("\nDesea encriptar el archivo de las contraseñas? Si (y) o No (n): "))
            encrip_archivo=encrip_archivo.upper()
        if (encrip_archivo=="S" or encrip_archivo=="SI"):
            encriptar(claves)
            print("\nSi desea desencriptar el archivo ejecute nuevamente el programa y elija la opción #5\n")
        elif (encrip_archivo=="N" or encrip_archivo=="NO"):
            print("\nGracias por elegir nuestros servicios.\n")
    else:
        print("\nGracias por elegir nuestros servicios.\n")

### Encriptar contraseñas ya existentes ###
elif (op_usuario==2):
    rpu_2=int(input("Ingrese el numero de contraseñas que desea encriptar: "))
    for i in range(rpu_2):
        if (i==0):
            password=[str(input("Ingrese la contraseña a encriptar: "))]
            password_encriptado = [generate_password_hash(password[i])]
        elif (i>0):
            password.append(str(input("Ingrese la siguiente contraseña a encriptar: ")))
            password_encriptado.append(generate_password_hash(password[i]))    
        cont=i+1
        print("\n")
        print("CONTRASEÑA NUMERO {} => {} => ENCRIPTADO NUMERO {} => {}".format(cont, password[i], cont, password_encriptado[i]))
        print("\n")
    save_or_not=int(input("\n1) Guardar las contraseñas. \n2) Salir. \nElegir una opción: "))
    if(save_or_not==1):
        ## Guardar contraseñas ##
        df_password=pd.DataFrame(password, columns=['CONTRASEÑAS'])
        claves=str(input("\nComo desea guardar las contraseñas: "))
        claves=claves+csv
        df_password.to_csv(claves, index=False)

        ## Guardar encriptado ##
        df_encriptado=pd.DataFrame(password_encriptado, columns=['CONTRASEÑAS ENCRIPTADAS'])
        encriptado=str(input("\nComo desea guardar las contraseñas encriptadas: "))
        encriptado=encriptado+csv
        df_encriptado.to_csv(encriptado, index=False)
   
    ## Encriptar archivo contraseñas ##
        encrip_archivo=str(input("\nDesea encriptar el archivo de las contraseñas? Si (s) o No (n): "))
        encrip_archivo=encrip_archivo.upper()
        while (encrip_archivo != "S" and encrip_archivo != "SI" and encrip_archivo != "N" and encrip_archivo != "NO"):
            encrip_archivo=str(input("\nDesea encriptar el archivo de las contraseñas? Si (y) o No (n): "))
            encrip_archivo=encrip_archivo.upper()
        if (encrip_archivo=="S" or encrip_archivo=="SI"):
            encriptar(claves)
            print("\nSi desea desencriptar el archivo ejecute nuevamente el programa y elija la opción #5\n")
        elif (encrip_archivo=="N" or encrip_archivo=="NO"):
            print("\nGracias por elegir nuestros servicios.\n")

    else:
        print("\nGracias por elegir nuestros servicios.\n")


### Mostrar contraseñas ya encriptadas ###
elif (op_usuario==3):
    from B_verificar_contraseña import check
    print("\nPor favor asegurese que el archivo donde se encuentran las contraseñas no este encriptado.")
    print("Si no esta seguro, reinice el programa y presione en el menu la opción #5")
    archivo=str(input("\nIngrese el nombre del archivo donde se encuentran las contraseñas: "))
    archivo=archivo+csv
    if (exists(archivo)==True):
        rpu_3=str(input("\nIngrese el encriptamiento: "))
        rpu_3=rpu_3.replace(" ", "")
        check(archivo, rpu_3)
    else:
        print("\nEl archivo con el nombre ingresado no existe.\n")

### Encreiptar archivo ###
elif (op_usuario==4):
    encriptar(str(input("\nIngrese el nombre el archivo: "))+csv)

### Desencriptar archivo ###
elif (op_usuario==5):
    desencriptar(str(input("\nIngrese el nombre el archivo: "))+csv)

###  Salir del programa ###
else:
    print("\nGracias por elegir nuestros servicios.\n")

