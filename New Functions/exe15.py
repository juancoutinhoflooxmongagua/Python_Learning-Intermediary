from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 9.90},
]


def function(total, produto):
    print('acumulador', total)
    print('produto', produto)
    print()
    return produto['preco']
    
total = reduce(
    function,
    produtos,
    0
)