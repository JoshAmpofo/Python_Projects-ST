fname = input('Enter a filename: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
