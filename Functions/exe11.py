import copy

d1 = {
    'c1': 1,
    'c1': 2,
    'l1': [0, 1, 3]
}

d2 = copy.deepcopy(d1)

d2['c1'] =1000
d2['l1'][0] = 1111
print(d2)
print(d1)