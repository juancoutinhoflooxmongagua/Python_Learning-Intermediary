p1 = {
    'nome': 'Luiz',
    'lastnome': 'Miranda'
}

print(p1.get('nome'))


nome = p1.pop('nome')

print(nome)
print(p1)

p1.update({
    'nome' : 'novo valor'
})

print(p1)
