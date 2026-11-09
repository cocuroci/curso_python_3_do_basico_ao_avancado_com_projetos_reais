"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[5]) # u
print(variavel[-3]) # n
print(variavel[4:]) # mundo
print(variavel[4:8]) # mund
print(variavel[0:5]) # Olá m
print(variavel[:5]) # Olá m
print(len(variavel[3])) # 1
print(len(variavel[4:8])) # 4
print(variavel[::2]) # Oámno (pulou de 2 em 2)
print(variavel[::-1]) # odnum álO (inverteu)