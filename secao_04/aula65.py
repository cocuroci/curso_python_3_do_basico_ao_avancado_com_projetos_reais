'''
Introduções a funcoes (def) em Python
FUnções são trechos de ódigo usados para
replicar determinada ação ao longo do seu código
Elas podem receber valores para parametros (argumentos)
e retornar um valor especifico
Por padrão, funções Python retornam None (nada)
'''

def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 3)
imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}')

saudacao('Andre')
saudacao()