"""This program records the domain name of where messages were sent from and prints total number of domain names
emails have come from"""
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: %s does not exist!' % fname)
    quit()

count = dict()
for line in fhand:
    if line.startswith('From '):
        line = line.rstrip()
        word = line.split()
        words = word[1]
#        print(words)
        new_words = words.split('@')
        new_line = new_words[1]
#        print(new_words[1])
        count[new_line] = count.get(new_line, 0) + 1
print(count)
