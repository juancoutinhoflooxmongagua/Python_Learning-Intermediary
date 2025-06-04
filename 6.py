def gen():
    yield 1
    yield 2
    yield 3

def gen2(gen_func): 
    yield from gen_func()
    yield 4
    yield 5

g = gen2(gen) 

for n in g:
    print(n)