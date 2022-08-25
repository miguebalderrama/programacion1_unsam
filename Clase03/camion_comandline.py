#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mbalderr
"""
import csv
import sys

def costo_camion(nombre_archivo):
    precio_total = 0
    precio_cajon = 0
    cant_cajones = 0
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)        
    for row in rows:                   
        precio_cajon = (float(row[2].strip('\n'))) 
        cant_cajones = (float(row[1])) 
        precio_total = precio_total + (precio_cajon * cant_cajones)
    f.close()    
    return precio_total

 
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)
