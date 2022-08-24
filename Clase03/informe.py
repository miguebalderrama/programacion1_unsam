# fragmento de costo_camion.py
import csv

def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    lote = {}
    camion = []
    total = 0   
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:                           
                lote['nombre'] = row[0]                 
                lote['precio'] = int(row[1])
                lote['cajones'] = float(row[2])
                camion.append(lote)
                lote = {}
        for s in camion:
            total+= s['cajones']*s['precio']        
        return total

def leer_precios(nombre_archivo):
    fruta_precio = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows):
                if row:                 
                 fruta_precio[row[0]] = float(row[1])  
                else:
                    continue
    return fruta_precio


 
                
precios = leer_precios('../Data/precios.csv')
print(precios['Cereza'])
precio_total = leer_camion('../Data/camion.csv')
print(precio_total) 


