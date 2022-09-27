import random

def tirar(nroDados):
 tirada=[]
 for i in range(nroDados):
    tirada.append(random.randint(1,6)) 
 print(tirada)
 return tirada

def es_generala(tirada):
    result = False
    long = len(tirada) - 1    
    for i, z in enumerate(tirada):        
        if i < long:          
          if z == tirada[i+1]:
              result = True
          else: 
              result = False
              break
        else:
            break
    return result

def prob_generala():
    nroDados = 5
    freqmax = 0
    nroturno = 0
    while nroturno < 3:
      nroDados = 5 - freqmax
      tirada = tirar(nroDados)      
      for i, z in enumerate(tirada):
        frecuencia = tirada.count(z)
        if frecuencia > freqmax:
             freqmax= frecuencia
             valor = z
      nroturno += 1
    
    return (freqmax ,valor)



#tiro = tirar()
#resultado = es_generala(tiro)
#print("El resultado es:", resultado)
#N = 1000
#G = sum([es_generala(tirar(5)) for i in range(N)])
#prob = G/N
#print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
#print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
resultado = prob_generala()
print("La frecuencia y el valor ", resultado)

 