fname = input('Enter a file: ')
if len(fname) < 1: fname = 'clown.txt'
fhand = open(fname)

di = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        di[word] = di.get(word, 0) + 1
# print(di)

tmp = list()
for k, v in di.items():
    tup = (v, k)
    tmp.append(tup)

tmp_2 = sorted(tmp, reverse=True)
# print(tmp_2)
for v, k in tmp_2[:5]:
    print(k, v)
