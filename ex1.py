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

days = 0
temp = []
temp_m = 0
menor_temp = 0
maior_temp = 0
temp_in_m = 0

# ENTRADAS

print('========== TEMPERATURAS DIÁRIAS ==========\n')
days = int(input('Entre com o número de dias: '))
print('Entre com uma temperatura entre 15 e 40 graus.')
for i in range(days):
    temp = float(input(f'Entre com {i + 1}° temperatura - '))
    if temp >= 15 and temp <= 40:
        continue
    else:
        print('Entre com uma temperatura valida!')
        continue

# PROCESSAMENTO

menor_temp = min(temp)

# SAIDA

print('============= RESULTADO ===============')
print(f'Menor temperatura - {menor_temp}°.')
print(f'Maior temperatura - {maior_temp}°.')
print(f'Temperatura média - {temp_m:.2f}°.')
print(f'Dias que a temperatura foi inferior a média - {temp_in_m}.')
