import random
import string
import numpy as np


def medir_temp(n):
 
 lista = []
 for i in range(n):
        valor = 37.5 +(random.normalvariate(0,0.2))
        lista.append(valor)
 a = np.array(lista)
 np.save('../Data/temperaturas.npy', a) 
 return lista

valores_med = medir_temp(999)
print(f'los valores medidos son:',valores_med)