import random

nine_digits = ''
for i in range(9):
    nine_digits += str(random.randint(0, 9))

print(nine_digits)

countdown_timer_first = 10
result_first_digit = 0

for digit in nine_digits:
    result_first_digit += int(digit) * countdown_timer_first
    countdown_timer_first -= 1

result_first_digit = (result_first_digit * 10) % 11
first_digit = 0 if result_first_digit > 9 else result_first_digit

print(f'Soma 9 digitos é {result_first_digit}')
print(f'Resultado da conta é {result_first_digit}')
print(f'O primeiro digito do CPF é {first_digit}')

second_cpf_value = nine_digits + str(first_digit)
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

cpf_gerado = f'{nine_digits}{first_digit}{second_digit}'

print(cpf_gerado)