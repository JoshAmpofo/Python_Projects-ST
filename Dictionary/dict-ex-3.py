"""This program reads through a mail log, builds a histogram using a dictionary and
counts the number of messages that have come from each email address."""
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
        count[words] = count.get(words, 0) + 1
print(count)
