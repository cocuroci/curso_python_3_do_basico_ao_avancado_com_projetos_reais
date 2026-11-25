# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest

def zipper(l1, l2):
    interval = min(len(l1), len(l2))
    return [(l1[i], l2[i]) for i in range(interval)]

cities = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states = ['BA', 'SP', 'MG', 'RJ']

# without zip
print('without zip', zipper(cities, states), sep=' => ')

# with zip
result = list(zip(cities, states))
print('with zip', result, sep=' => ')

# with zip_longest
print('with zip_longest', list(zip_longest(cities, states, fillvalue='Sem cidade')),  sep=' => ')
