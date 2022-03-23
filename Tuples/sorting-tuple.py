# d = {'a': 10, 'b': 1, 'c': 22}
# # print(d.items())
# t = sorted(d.items())
# for k, v in t:
#     print(k, v)

"""Sorting by values instead of keys"""
c = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))
print(tmp)

# tmp_2 = sorted(tmp, reverse=True)
# print('Reverse:', tmp_2)