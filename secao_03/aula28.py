"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou os campos"
"""
name = input('Digite seu nome: ')
age = input('Digite sua idade: ')

def print_informations(name):
    print(f'Seu nome é {name}')
    print(f'Seu nome invertido é {name[::-1]}')
    print(f'Seu nome tem espaço? {' ' in name}')
    print(f'Seu nome tem {len(name)} letras')
    print(f'A primeira letra do seu nome é {name[0]}')
    print(f'A útima letra do seu nome é {name[-1]}')

if len(name) > 0 and len(age) > 0:
    print_informations(name)
else:
    print('Desculpe, você deixou os campos vazios.')