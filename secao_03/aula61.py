"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

import re
import sys

cpf_enviado = '746.824.890-70'
#cpf_only_numbers = cpf_enviado.replace('.','').replace('-','')
cpf_only_numbers = re.sub(r'[^0-9]', '', cpf_enviado)
first_nine_digits = cpf_only_numbers[:9]
list_digits = []

is_sequential = cpf_only_numbers == cpf_only_numbers[0] * len(cpf_only_numbers)

if is_sequential:
    print('A entrada é sequencial')
    sys.exit()

countdown_timer_first = 10
for digit in first_nine_digits:
    list_digits.append(int(digit) * countdown_timer_first)
    countdown_timer_first -= 1

sum_nine_digits = sum(list_digits)

result_first_digit = (sum_nine_digits * 10) % 11
first_digit = 0 if result_first_digit > 9 else result_first_digit

print(f'Soma 9 digitos é {sum_nine_digits}')
print(f'Resultado da conta é {result_first_digit}')
print(f'O primeiro digito do CPF é {first_digit}')

second_cpf_value = first_nine_digits + str(first_digit)
countdown_timer_second = 11
result_second = 0

for digit in second_cpf_value:
    result_second += int(digit) * countdown_timer_second
    countdown_timer_second -= 1

result_second_digit = (result_second * 10) % 11
second_digit = 0 if result_second_digit > 9 else result_second_digit

print(f'Soma 10 digitos é {result_second}')
print(f'Resultado da conta é {result_second_digit}')
print(f'O segundo digito do CPF é {second_digit}')

cpf_gerado = f'{first_nine_digits}{first_digit}{second_digit}'

if cpf_gerado == cpf_only_numbers:
    print(f'{cpf_enviado} é um CPF válido')
else:
    print('CPF inválido')