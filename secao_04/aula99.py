from sys import path

import aula99_packaged.modulo
# ou 
from aula99_packaged import modulo
# ou
from aula99_packaged.modulo import soma_do_modulo

from aula99_packaged.modulo_b import fala

print(*path, sep='\n')
print(__name__)
print(aula99_packaged.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(4, 2))
print(soma_do_modulo(2, 2))

fala(f'oi dentro do {__name__}')