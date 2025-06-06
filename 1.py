

def adiciona_clientes(nome, lista=[]):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

lista1 = []

cliente1 = adiciona_clientes('Juan', lista1)

adiciona_clientes('João', cliente1)

print(cliente1)