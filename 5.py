

def generator(n=0):
    yield 1
    print('Continuando...')
    yield 2
    print('Quase lá')
    return 'Acabou'

gen = generator(n=0)

for n in gen:
    print(n)