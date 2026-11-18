# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são 'Syntax Sugar'

# func decoradora
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna

def inverte_string(string):    
    return string[::-1]

# usando decoradora
@criar_funcao
def inverte_string_decorada(string):    
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser string')
    return True

# Sem usar func decoradora
invert_string_checando_parametro = criar_funcao(inverte_string)
invertida = invert_string_checando_parametro('André Cocuroci')
print(invertida)
print()

# USando decoradora
invertida_string = inverte_string_decorada('André José')
print(invertida_string)