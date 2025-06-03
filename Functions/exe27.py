


product = {
    'name': 'caneta',
    'price': '0.3',
    'category': 'Work',
}

'''

for key, value in product.items():
   print(key, value)

'''

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in product.items()
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]
dc = {
    chave: valor
    for chave, valor in lista
}

s1 = {2 ** i for i in range(10)}
print(s1)