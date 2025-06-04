import sys

iterable = ['eu', 'tenho', '__iter__']

iterator = iter(iterable)


gen = (n for n in range(9))
lista = [n for n in range(9)]

print(sys.getsizeof(gen))
print(sys.getsizeof(lista))