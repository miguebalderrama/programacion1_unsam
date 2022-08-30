# lectura de parques de la Ciudad de Buenos Aires

import csv

def leer_parque(nombre_archivo,parque):
    '''Lectura de parques de un archivo base de caba'''
   ## lote = {}
    lista_arboles = []    
    with open(nombre_archivo, 'rt', encoding="utf8") as f:
        rows = csv.reader(f)
        cont = 0
        headers = next(rows)               
        for row in rows:  
            if parque in row:                    
                d = dict(zip (headers,row))                     
                
                lista_arboles.append(d)
    return lista_arboles

def especies(lista_arboles):
    listado = []
    for lista in lista_arboles:
        listado.append(lista['nombre_com'])
    unicos = set(listado)
    print(unicos)




    
arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', "GENERAL PAZ")
lista_especi = especies(arboles)
print(lista_especi)