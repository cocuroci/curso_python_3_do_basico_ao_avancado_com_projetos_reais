"""
for in com listas
"""

lista = ['Maria', 'Melena', 'JoÃO']

for item in lista:
    print(item)

start_with_m = [x for x in lista if x.startswith('M')]

print(lista)
print(start_with_m)