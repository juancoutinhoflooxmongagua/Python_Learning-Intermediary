


# Funções Recursivas


def recursiva(inicio=0, fim=10):
    if inicio >= fim:
        return fim 
    print(inicio, fim)
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())


def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))