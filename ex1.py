#########################
#
# Nome: Arlenson Lorran
#
# Data: 24/09/2024
#
#########################

# IMPORTAR BIBLIOTECAS

import time as t

# OPERANDOS

temp1 = 0
temp2 = 0
temp3 = 0
temp_m = 0
menor_temp = 0
maior_temp = 0
temp_in_m = 0

# ENTRADAS

print('========== TEMPERATURAS DIÁRIAS ==========\n')
temp1 = float(input('Entre com a 1º temperatuda - '))
temp2 = float(input('Entre com a 2º temperatuda - '))
temp3 = float(input('Entre com a 3º temperatuda - '))

# PROCESSAMENTO

menor_temp = min(temp1, temp2, temp3)
maior_temp = max(temp1, temp2, temp3)
temp_m = (temp1 + temp2 + temp3) / 3
if temp1 < temp_m:
  temp_in_m += 1
if temp2 < temp_m:
  temp_in_m += 1
if temp3 < temp_m:
  temp_in_m += 1

# SAIDA

t.sleep(1)
print('\n============= RESULTADO ===============\n')
print(f'Menor temperatura - {menor_temp}°.')
print(f'Maior temperatura - {maior_temp}°.')
print(f'Temperatura média - {temp_m:.2f}°.')
print(f'Dias que a temperatura foi inferior a média - {temp_in_m}.')
