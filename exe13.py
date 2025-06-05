from itertools import groupby

alunos = ['a', 'b', 'c']

grupos = groupby(alunos)

print(grupos)

for grupo in grupos:
    print(grupo)