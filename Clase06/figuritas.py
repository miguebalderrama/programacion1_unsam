import random
import numpy as np
import random



figuritas_total = 670
n_repeticiones = 100
############## FUNCIONES #######################################
def crear_album(figus_total):
    album = np.zeros(shape=figus_total)
    return album

def album_incompleto(A):
    if 0 in A:
        return True
    else:
        return False

def comprar_figu(figus_total):
    figu_toca = random.randint(1,figus_total) # devuelve un entero aleatorio entre 1 y 6
    return figu_toca

def cuantas_figus(figus_total):
    cant_figus = 0  
    album = crear_album(figus_total)
    while album_incompleto(album):
        figurita = comprar_figu(figus_total)
        cant_figus += 1
        for i, n in enumerate(album):
            if figurita == i+1:
                album[i] = 1                         
              
    return cant_figus

def experimento_figus(n_repeticiones, figus_total):
    lista = []
    for x in range(n_repeticiones):
        cantidad = cuantas_figus(figus_total)
        lista.append(cantidad)
    array = np.array(lista)
    print(array)
    promedio = np.mean(array)
    return promedio
    


################# IMPLEMENTACION ############################
promedio = experimento_figus(n_repeticiones,figuritas_total)
print( "En promedio debemos comprar", promedio, "figuritas.")


    







