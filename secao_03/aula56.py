'''
split e join com list e str
split - divide uma string
join - une uma string
'''

frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split()
lista_frases = frase.split(',')
print(lista_palavras, lista_frases)

frases_unidas = '-'.join(lista_palavras)
print(frases_unidas)