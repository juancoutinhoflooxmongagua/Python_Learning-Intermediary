def fora(x):
    a = x

    def  dentro():
        return a
    return dentro

dentro = fora(1)
print(dentro())