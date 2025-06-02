

x, y, *_resto = 1, 2, 3, 4


def soma(*args):
    total = 0 
    for number in args:
        total += number
        print(f'Numero somado: {number} igual: {total}')

soma(1,2,3,4)

n1 = input('primeiro numero: ')
in1 = int(n1)
n2 = input('segundo numero: ')
in2 = int(n2)
n3 = input('terceiro numero: ')
in3 = int(n3)

numbers = soma(in1, in2, in3)

print(sum((1,2,3,4)))