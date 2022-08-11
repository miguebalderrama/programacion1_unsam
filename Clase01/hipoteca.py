# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca

saldo = 500000.0
tasa = 0.05
cuota_fija = 2684.11
cuota_ajustada = 0
pago_mensual = 0
pago_extra = 1000.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
cantMesesAdelanto = 12
total_pagado = 0
mes = 0

while saldo > 0:
    mes = mes + 1
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        pago_mensual = cuota_fija + pago_extra
    else:
        pago_mensual = cuota_fija        
    saldo = saldo * (1+tasa/12) - pago_mensual
    if saldo < 0:
        cuota_ajustada= saldo + pago_mensual
        saldo = saldo + pago_mensual -cuota_ajustada
        
    total_pagado = total_pagado + pago_mensual    
    print (mes,pago_mensual,total_pagado,saldo)

print('Total pagado', round(total_pagado, 2))
print('Total de meses', mes)
print('Valor ajustado ultima cuota', cuota_ajustada)