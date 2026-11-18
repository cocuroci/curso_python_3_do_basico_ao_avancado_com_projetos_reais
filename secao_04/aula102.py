# Variaveis livres + nonlocal

""" def fora(x):
    a = x

    def dentro():
        print(locals())
        return a

    return dentro

dentro_1 = fora(1)
dentro_2 = fora(2)

print(dentro_1())
print(dentro_2()) """

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final

    return interna

concatenar_nomes = concatenar('Marci')
print(concatenar_nomes(' Ama André'))
print(concatenar_nomes(' E Helena'))
