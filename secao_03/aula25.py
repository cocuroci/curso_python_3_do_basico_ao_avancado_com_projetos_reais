"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'André'
preco = 1000.9568
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecual de %d é %x' % (15,15))
print('O hexadecual de %d é %X' % (15,15))
print('O hexadecual de %d é %04X' % (15,15))
print('O hexadecual de %d é %08X' % (15,15))