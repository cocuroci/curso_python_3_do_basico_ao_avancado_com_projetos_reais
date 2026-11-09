# Calculadora com while
operadores_permitidos = '+-/*'

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input(f'Digite o operador ({operadores_permitidos}): ')
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue

    if len(operador) > 1:
        print('Digite somente 1 operador')
        continue

    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')

    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)

    if operador == '-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)

    if operador == '/':
        print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)

    if operador == '*':
        print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)

    sair = input('Quer sair? [s]im: ')
    if sair.lower().startswith('s'):
        break