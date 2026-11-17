# Usado para quando o import for from nome_modulo import * 
# (o __all__ controla quais variaveis/metodos pode ser usados. Sem eles todos ficam disponívels)
__all__ = [
    'soma_do_modulo'
]

from aula99_packaged.modulo_b import fala

def soma_do_modulo(x, y):
    return x + y

fala(f'oi dentro de: {__name__}')