

def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def executa(function, x):
    def interna(y):
        return function(x, y)
    return interna

soma = executa(soma, 4)
print(soma(2))