# (Parte1) try e except para tratar exceções
a = 18
b = 0

try:
    print('Linha 1'[9999]) #IndexError
    c = a / b #ZeroDivisionError
    print('Linha 2, não será executado')
except ZeroDivisionError as error:
    print(f'{error=}')
except (NameError, IndexError) as error:
    print(f'{error=}')
    print('Erro:', error.__class__.__name__)
except Exception:
    print('Erro desconhecido (Sem tratar error)')

print('Continuar')