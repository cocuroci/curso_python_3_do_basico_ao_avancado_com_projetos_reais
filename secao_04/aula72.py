# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiply_all(*args):
    total = 1
    for n in args:
        total *= n
    return total

def is_it_even_or_odd(value):
    message = f'O número {value} é'
    return f'{message} par' if value % 2 == 0 else f'{message} impar'


print(1 * 2 * 3)
print(multiply_all(1, 2, 3))
print(is_it_even_or_odd(5))