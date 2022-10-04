import pandas as pd
from werkzeug.security import check_password_hash

def check(archivo, rpu_3):
    datos = pd.read_csv(archivo)
### Count the number of existing passwords ###
    with open(archivo) as myfile:
     total_lines = sum(1 for line in myfile)
### Iterate through each row of the file ###
    for i in range(total_lines-1):
        pass_word=datos.iat[i,0]
### Check every encryption with every password ###
        if(check_password_hash(rpu_3, pass_word)==True):
            print("\nThe password is: ", pass_word, "\n")
            return
        elif (i==(total_lines-2)):
            print("\nThe encrypted does not belong to none password inside file.\n")