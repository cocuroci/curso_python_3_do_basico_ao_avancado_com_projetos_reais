from datetime import date

nome = 'André'
sobrenome = 'Martins'
idade = 44
ano_nascimento = date.today().year - idade
maior_de_idade = idade >= 18
altura_metros = 1.67

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('Maior de idade:', maior_de_idade)
print('Altura em metros:', altura_metros)