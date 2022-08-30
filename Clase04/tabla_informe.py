# fragmento de costo_camion.py
import csv

def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    
    camion = []    
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows: 
                lote = {}                          
                lote['nombre'] = row[0] # Asignament to dict. values of fruit                 
                lote['cajones'] = int(row[1])
                lote['precio'] = float(row[2])
                camion.append(lote) # add the data of one fruit to the list                           
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

def hacer_informe(lista_camion,precios_venta):
       listar_frutas = []
       print('    Nombre    Cajones     Precio     Cambio')
       print('---------- ---------- ---------- ----------')
       for r in lista_camion:
        nombre = r['nombre']                
        if nombre in precios_venta:
            cambio = precios_venta[nombre] - r['precio']
        c = (r['nombre'],r['cajones'],'$'+str(r['precio']), cambio ) # convierto a string para agregar el signo $
        print('%10s %10d %10s %10.2f' % c)
        listar_frutas.append(c)
       

 
                
precios_venta = leer_precios('../Data/precios.csv')
lista_camion = leer_camion('../Data/camion.csv')
balance_total = balance(lista_camion, precios_venta) 
print("Nos queda de ganancia:", balance_total)
informe = hacer_informe(lista_camion, precios_venta)



