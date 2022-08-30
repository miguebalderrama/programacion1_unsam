headers = ( "       0   1   2   3   4   5   6   7   8   9" )
separator = ("---------------------------------------------")
fila = []
print(headers)
print(separator)
for i in range(0, 10):       
 for c in range(0, 10):        
        fila.append(c*i)
 r = (str(i)+":", fila[0],fila[1], fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9] )
 print('%1s %5d %3d %3d %3d %3d %3d %3d %3d %3d %3d' %r)
 fila = []


    



