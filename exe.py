import copy

produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(oroduto, porcentagem):
    for produto in produtos:
        produto['preco'] += (1 + porcentagem / 100)

aumentar_porcentagem(produtos, 10)

print(produtos)