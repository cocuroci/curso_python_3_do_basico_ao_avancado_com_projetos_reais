nome = 'André'
altura = 1.67
peso = 65
imc = peso / altura ** 2

print(f'{nome} tem {altura} de altura, pesa {peso} quilos e seu IMC é {imc:.2f}.')
print('{} tem {} de altura, pesa {} quilos e seu IMC é {:.2f}.'.format(nome, altura, peso, imc))