
"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

count = 0

while count < 100:
    count += 1

    if count == 6:
        print(f'Não vamos printar o {count}')
        continue

    print(f'Contanto {count:02d}')

    if count == 40:
        print(f'O contador chegou a {count} e vamos dar um break')
        break

print('acabou')