from itertools import combinations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

person = [ 
    'João', 'Joana ', 'Luiz'
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm'],
    ['Fem', 'Masc']
]

#print(combinations(person, 2))
#print_iter(combinations(person, 2))


print_iter(product(*camisetas))