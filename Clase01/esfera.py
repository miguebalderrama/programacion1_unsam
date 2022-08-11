# esfera.py
# Archivo de ejemplo
# Ejercicio de volumen de esfera

import math
valido = False

while valido == False:
    radio = input('Ingrese radio de la esfera:')
    valido = radio.isnumeric()
    if valido == False: 
        print ("Debe ingresar un valor numerico positivo, vuelva a intentarlo.")    

volumen =(4/3) * math.pi * (float(radio) ** 3)
print ("El volumen de la esfera es :", volumen)
