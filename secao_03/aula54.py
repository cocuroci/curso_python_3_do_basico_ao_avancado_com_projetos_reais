"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import subprocess

lista = []

def clear_terminal():
    subprocess.call('cls', shell=True)

while True:
    print('Selecione uma opção: ')
    opcao = input('[i]nserir, [a]pagar, [l]istar, [s]air: ').strip().lower()

    if opcao == 'i':
        clear_terminal()
        valor = input('Valor: ')

        if valor:
            lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            clear_terminal()
            print('Indice inválido')

    elif opcao == 'l':
        clear_terminal()
        if lista:
            for index, value in enumerate(lista):
                print(index, value)
        else:
            print('Lista vazia')

    elif opcao == 's':
        clear_terminal()
        print('Saindo do programa')
        break