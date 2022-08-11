# rebotes.py
# Archivo de ejemplo
# Ejercicio

altura = 100 # Altura inicial del salto
rebote = 0 # Rebotes
constanteRebote = 0.6 # constante de rebote

while rebote < 10:
    altura = altura * constanteRebote
    rebote = rebote + 1
    print(rebote, altura)
