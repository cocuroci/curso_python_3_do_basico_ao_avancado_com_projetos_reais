# dir, hasattr e getattr em Python

string = 'André'
metodo = 'upper'

if hasattr(string, metodo):
    print(f'Existe o metodo {metodo}', string.upper())
    print(getattr(string, metodo)) #pega o metodo dinamicamente
    print(getattr(string, metodo)()) #executa o método
else:
    print(f'Não existe o {metodo=}')