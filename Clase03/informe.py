# fragmento de costo_camion.py
import csv

def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    lote = {}
    camion = []    
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:                           
                lote['nombre'] = row[0] # Asignament to dict. values of fruit                 
                lote['cajones'] = int(row[1])
                lote['precio'] = float(row[2])
                camion.append(lote) # add the data of one fruit to the list
                lote = {} # Declare again the dict             
        return  camion

def leer_precios(nombre_archivo):
    fruta_precio = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)       
        for i, row in enumerate(rows):
                if row:                 
                 fruta_precio[row[0]] = float(row[1])  
                else:
                    continue
    return fruta_precio

def balance (lista_camion, precio_venta):     
     total = 0
     total_venta = 0
     for s in lista_camion:            
            total+= s['cajones']*s['precio']           
     for row in lista_camion:
        nombre = row['nombre']        
        if nombre in precio_venta:                
                total_venta += row['cajones']*precio_venta[nombre]           
     return total_venta-total
 
                
precios_venta = leer_precios('../Data/precios.csv')
lista_camion = leer_camion('../Data/camion.csv')
balance_total = balance(lista_camion, precios_venta) 
print("Nos queda de ganancia:", balance_total)



