
def make_multiply(x):
    def multiply(y):
        return x * y
    return multiply

x = input('Digite o numero que vc quer multiplicar: ')

duplicar = make_multiply(2)
triplicar = make_multiply(3)
quadruplicar = make_multiply(4)

print(f'Duplicado:',duplicar(int(x)))
print(f'Triplicado:',triplicar(int(x)))
print(f'Quadruplicado:',quadruplicar(int(x)))