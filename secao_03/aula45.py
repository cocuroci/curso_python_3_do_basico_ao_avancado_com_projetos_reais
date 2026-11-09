"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

texto = 'André Cocuroci'
iteratador = iter(texto)

while True:
    try:
        print(next(iteratador))
    except StopIteration:
        break