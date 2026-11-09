"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

condicao = None
while condicao is None:
    nome = input('Qual seu nome: ')

    if len(nome) > 0:
        print(f'Seu nome é {nome}')
        condicao = False