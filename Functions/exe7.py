


def hello(hello):
    def say_hello(name):
        return f'{hello}, {name}'
    return say_hello

h1 = hello('Olá')
h2 = hello('Tchau')

print(h1('Juan'))
print(h2('Juan'))