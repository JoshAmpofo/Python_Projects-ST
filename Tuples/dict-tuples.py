# t = {'a': 10, 'b': 1, 'c': 22}
# d = list(t.items())
# print(d)

# d.sort()  # redundant
# print(d)  # redundant

# for key, value in list(t.items()):
#    print(value, key)

# t = {'a': 10, 'b': 1, 'c': 22}
# m = list()
#
# for key, val in t.items():
#     m.append((val, key))
# print('Non-reversed:', m)
#
# m.sort(reverse=True)
# print('Reversed:', m)

di = dict()
di['csev'] = 2
di['cwen'] = 4

for (k, v) in di.items():
    print(k, v)

# tups = di.items()
# print(tups)
