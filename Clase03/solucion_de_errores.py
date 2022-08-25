import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:            
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro) # registro es un puntero al diccionario original, al cargar nuevo valor siempre apunta a la misma direccion y no se signa nuevo valor 
            # tenemos que declarar de nuevo el diccionario en cada lazo para que se asigne nuevos valores.
            registro = {} 
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)