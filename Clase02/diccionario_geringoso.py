# geringoso.py
# Archivo de ejemplo
# Ejercicio de geringoso

cadena = "Geringoso"
cadenageringoso = ""
for c in cadena:  
  if c == "e" :
   c = c.replace( c,c+"pe")
   cadenageringoso = cadenageringoso + c
  elif  c == "a" :
   c = c.replace( c,c+"pa")
   cadenageringoso = cadenageringoso + c
  elif  c == "i" :
   c = c.replace( c,c+"pi")
   cadenageringoso = cadenageringoso + c
  elif  c == "o" :
   c = c.replace( c,c+"po")
   cadenageringoso = cadenageringoso + c
  elif  c == "u" :
   c = c.replace( c,c+"pu")
   cadenageringoso = cadenageringoso + c
  else:
   cadenageringoso = cadenageringoso + c
 
print(cadena)
print(cadenageringoso)