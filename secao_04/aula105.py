# Decoradores com parâmetros
def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decorandora 1')
        def aninhada(*args, **kwargs):
            print('Parametro do decorador,', a, b, b)
            print('Aninhada')
            resultado = func(*args, **kwargs)
            return resultado
        return aninhada
    return fabrica_de_funcoes

@fabrica_de_decoradores(1, 2, 3)
def soma(x ,y):
    return x + y

decorador = fabrica_de_decoradores()
multiplica = decorador(lambda x, y:  x * y)
print(multiplica(2,3))