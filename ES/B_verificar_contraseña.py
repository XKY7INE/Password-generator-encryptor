import pandas as pd
from werkzeug.security import check_password_hash

def check(archivo, rpu_3):
    datos = pd.read_csv(archivo)
### Contar el numero de contraseñas existentes ###
    with open(archivo) as myfile:
     total_lines = sum(1 for line in myfile)
### Iterar en cada una de las filas del archivo ###
    for i in range(total_lines-1):
        pass_word=datos.iat[i,0]
### Comprobar cada encriptado con cada contraseña ###
        if(check_password_hash(rpu_3, pass_word)==True):
            print("\nLa contraseña es: ", pass_word, "\n")
            return
        elif (i==(total_lines-2)):
            print("\nEl encriptado no pertenece a ninguna de las contraseñas dentro de archivo.\n")