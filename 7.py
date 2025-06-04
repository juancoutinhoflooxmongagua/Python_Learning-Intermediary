
try:
    a = 18
    b = 2
    c = a / b    

except ZeroDivisionError:
    print('Dividiu por zero')
except NameError:
    print('O nome B n está definido')
print('Continuando')
print(c)