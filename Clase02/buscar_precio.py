#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mbalderr
"""
def buscar_precio(fruta):
    nombre_fruta = ""   
    nombre_archivo = '../Data/camion.csv'
    precio_fruta = 0

    with open(nombre_archivo, 'rt') as f:
        next(f)
        for line in f:            
            row = line.split(',') 
            nombre_fruta = row[0] 
            if nombre_fruta == fruta :
                precio_fruta = float(row[2].strip('\n')) 
                print('El precio de un cajon de', fruta, 'es:', str(precio_fruta) ) 
                return            
    print(fruta, 'no figura en el listado de precios.' ) 

    

buscar_precio("Lima")
