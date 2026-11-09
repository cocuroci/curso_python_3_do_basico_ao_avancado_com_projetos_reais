# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')

s1 = set()  # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

set_values_duplicates = {1, 2, 3, 3, 3, 3, 1}
print(set_values_duplicates)

sample_list = [1, 2, 3, 3, 3, 3, 1]
set_remove_values = set(sample_list)
sample_list_remove_duplicates_values = list(set_remove_values)
print(sample_list, sample_list_remove_duplicates_values, set_remove_values)

print(3 in set_values_duplicates)
print(4 not in set_values_duplicates)

# Métodos úteis:
# add, update, clear, discard

s2 = set()
s2.add('Luiz')
s2.add(1)
s2.update({'Olá mundo', 1, 2, 3, 4})
print(s2)

s2.discard('Olá mundo')
print(s2)

s2.clear()
print(s2)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

print('=====================')

s3 = {1, 2, 3}
s4 = {2, 3, 4}

s5 = s3 | s4
print(s5)

s6 = s3 & s4
print(s6)

s7 = s3 - s4
print(s7)

s8 = s3 ^ s4
print(s8)