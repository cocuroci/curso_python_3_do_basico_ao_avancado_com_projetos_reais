"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
input_number = input('Digite um número inteiro: ')

try: # ou input_number.isdigit() no if
    converted_number = int(input_number)
    message = 'Par' if converted_number % 2 == 0 else 'Impar'
    print(f'O número {input_number} é {message}')
except:
    print('O texto digitado não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

input_hour_number = input('Digite a hora (apenas 0 até 23): ')

try:
    converted_hour_number = int(input_number)
    if converted_number >=0 and converted_number <= 11:
        print('Bom dia')
    elif converted_number >= 12 and converted_number <= 17:
        print('Boa tarde')
    else:
        print('Boa noite')
except:
    print('O texto digitado não é um número inteiro')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

input_name = input('Digite seu nome: ')
len_name = len(input_name)

if len_name <= 4:
    print('Seu nome é pequeno')
elif len_name > 4 and len_name <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
