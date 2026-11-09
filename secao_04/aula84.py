# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)

print(lista)
print()

lista_2 = [numero * 2 for numero in range(10)]

print(lista_2)

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30}
]

novos_produtos = [
    {**produto, 'preco': produto.get('preco') * 1.10} #map
    if produto.get('preco') > 20 else {**produto} # alguma regra (muda o preço somente se o valor for acima de 20)
    for produto in produtos
]

novos_produtos_filtro = [
    produto
    for produto in produtos
    if produto.get('preco') < 20 # filtro fica a direita/depois do for
]

print(novos_produtos)
print(novos_produtos_filtro)