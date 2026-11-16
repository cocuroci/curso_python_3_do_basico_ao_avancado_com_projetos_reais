# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True

def deve_ser_int_ou_float(n):
     if not isinstance(n, (int, float)):
          raise TypeError(f'{n} deve ser int ou float')

def divide(n, d):
    deve_ser_int_ou_float(d)
    deve_ser_int_ou_float(n)
    nao_aceito_zero(d)
    return n / d

print(divide(9, 1))
print(divide(9, 3))