# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print('Try')
    #8/0
except ZeroDivisionError:
    print('ZeroDivisionError')
else:
    print('Não deu erro')
finally:
    print('Finally')