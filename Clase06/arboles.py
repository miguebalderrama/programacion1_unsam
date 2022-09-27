# lectura de parques de la Ciudad de Buenos Aires

import csv
from collections import Counter
import os
import matplotlib.pyplot as plt
import numpy as np

def leer_arboles(nombre_archivo,nom_arbol):
    '''Lectura de parques de un archivo base de caba'''
   
    lista_arboles = []    
    with open(nombre_archivo, 'rt', encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)               
        for row in rows:  
            if nom_arbol in row:
                                  
                d = dict(zip (headers,row))                   
                lista_arboles.append(d)
    return lista_arboles

os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv',"Jacarandá")
##print(arboleda)
altos = [(int (arbol['altura_tot']),int(arbol['diametro'])) for arbol in arboleda]
arr = np.array(altos)

h,d  = np.hsplit(arr, 2)

plt.scatter(d,h)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")
#plt.hist(altos,bins=50)
plt.show()



