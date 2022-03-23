# opeining file and building dict list
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
# print(counts)

# creating tuple list
lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
# print(lst)

# sorting and printing ten common words in files
lst_2 = sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(key, val)
