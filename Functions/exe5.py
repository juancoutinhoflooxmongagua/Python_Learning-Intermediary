
total = 0

def soma(*args):
    global total
    for number in args:
       total += number
    print(total)

soma(2, 3)


if total % 2 == 0:
    print('O número é Par')
else:
    print('O número é Impar')
