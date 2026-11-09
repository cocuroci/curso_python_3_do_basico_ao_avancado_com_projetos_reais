"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
number_string = input('Vou dobrar o número que você digitar: ')

try:
    number_float = float(number_string)
    print('FLOAT:', number_float)
    print(f'O dobro de {number_string} é {number_float * 2:.2f}')
except Exception as e:
    print(f'Isso não é um número, {e}')