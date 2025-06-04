

lista = []
dict = {}
conjunto = set()
tupla = (2)
string = ''
inteiro = 0
flutuante = 0.3
nada = None
falso = False
interval = range(0)

def falsy(value):
    return 'falsy'if not value else 'truthy'


print(f'Test is', falsy(tupla))
print(f'Test is', falsy(nada))
print(f'Test is', falsy(falso))
print(f'Test is', falsy(interval))
print(f'Test is', falsy(flutuante))
