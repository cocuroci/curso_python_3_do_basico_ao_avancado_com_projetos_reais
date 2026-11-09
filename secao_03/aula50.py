'''
Exercicio
Exiba os indices da lista
'''

lista = ['Maria', 'Helena', 'Luiz']

for index, nome in enumerate(lista):
    print(index, nome)


nova_lista = lista.copy()
indices = range(len(nova_lista))

for index in indices:
    print(index, nova_lista[index])