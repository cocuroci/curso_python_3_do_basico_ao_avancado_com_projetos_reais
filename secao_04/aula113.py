# reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

def soma_total(total, produto):
    return total + produto['preco']

total = reduce(
    lambda total, produto: total + produto['preco'],
    produtos,
    0
)

print(total)

print(
    sum([v.get('preco') for v in produtos])
)