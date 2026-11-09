# manupulando chaves e valores em dicionários                                                                                                                                                                                                                                                       
# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'André',
    'sobrenome': 'Cocuroci',
    'idade': 44,
    'altura': 1.67,
    'endereços': [
        {'rua': 'tal', 'numero': 123},
        {'rua': 'outra', 'numero': 321}
    ]
}

# adicionar novas chaves
new_key = 'imc'
pessoa[new_key] = 23.45
print(pessoa)

# remover chave
del pessoa[new_key]
print(pessoa)

print('método len', len(pessoa))
print('método keys', pessoa.keys())
print('método values', pessoa.values())
print('método items', pessoa.items())

# default
print(pessoa.setdefault('imc', 0))

import copy

# copy
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0 , 1 ,2]
}

d2 = d1.copy() #(copia rasa)
d3 = copy.deepcopy(d1) #(copia funda)

d2['c1'] = 1000
d2['l1'][1] = 999999
d3['c1'] = 78
d3['l1'][1] = 876

print(d1)
print(d2)
print(d3)

# get
p1 = {
    'nome': 'André',
    'sobrenome': 'Cocuroci'
}

print(p1.get('nome'))

#pop
nome = p1.pop('nome')
print(p1, nome)

#popitem
ultima_chave = p1.popitem()
print(p1, ultima_chave)

p1.update({
    'nome': 'Novo valor'
})

# outro jeito
p1.update(nome='Andre', idade=44)

# pode receber um interavel
tupla = ('sobrenome', 'novo valor')
p1.update(tupla)