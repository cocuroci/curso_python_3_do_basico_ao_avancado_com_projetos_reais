# while/else
string = 'Valor-qualquer'
i = 0

while i < len(string):
    letra = string[i]
    print(letra)

    if letra == ' ':
        break

    i += 1
else:
    print('O else do while foi executado')
    print('não encontrei um espaço na string')

print('Fora do laço while')