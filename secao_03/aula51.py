'''
Introdução ao desempacotamento
'''

nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = ['Andre', 'Marci', 'Aline']
# nome1, nome2 = ['Andre', 'Marci', 'Aline'] #ERROR
# nome1, nome2, nome3 = ['Andre', 'Marci'] #ERROR
nome1, *resto = ['Andre', 'Marci', 'Aline']
print(nome1, resto)

nome_um, *_ = ['A', 'B', 'C']
_, nome_2, *_ = ['A', 'B', 'C']