# Generator expression, Iterables e interators em Python

import sys

iterable = ['Eu', 'tenho', '__iter__']
#iterator = iterable.__iter__()
iterator = iter(iterable)
lista = [n for n in range(100)]
generator = (n for n in range(100)) # dentro dos () cria um generator

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))