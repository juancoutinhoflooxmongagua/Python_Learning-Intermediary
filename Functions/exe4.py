

x, y, *_resto = 1, 2, 3, 4


def sum(*args):
    total = 0 
    for number in args:
        total += number
        print(number, total)

sum(1,2,3,4)


