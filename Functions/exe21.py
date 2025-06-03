


def execute(function, *args):
    return function(*args)

def soma(x, y):
    return x + y

def make_multiply(multiplicador):
    def multiplica(number):
        return number * multiplicador
        return multiplica


print(
    execute(
        lambda x, y: x + y,
        2, 3
    ),
    execute(soma, 2,3)
)