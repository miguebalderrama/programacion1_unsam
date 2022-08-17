#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mbalderr
"""
def costo_camion(nombre_archivo):
    precio_total = 0
    precio_cajon = 0
    cant_cajones = 0

    with open(nombre_archivo, 'rt') as f:
        next(f)
        for line in f:            
            row = line.split(',') 
            precio_cajon = (float(row[2].strip('\n'))) 
            cant_cajones = (float(row[1])) 
            precio_total = precio_total + (precio_cajon * cant_cajones)
        
    return precio_total

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo) 
