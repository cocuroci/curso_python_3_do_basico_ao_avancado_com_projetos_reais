"""
Interando strings com while
"""
nome = 'André Cocuroci'
tamanho = len(nome)
index = 0
nome_formatado = ''

while index < tamanho:
    nome_formatado += '*' + nome[index]
    index += 1

print(nome_formatado)