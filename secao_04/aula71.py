"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

def sum_all(*args):
    return sum(args)
    
print(sum_all(1,2,3))