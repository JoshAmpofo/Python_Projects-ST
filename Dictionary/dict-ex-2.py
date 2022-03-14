"""This program categorizes each mail message by day of week the commit was done.
And returns the total number of days in which mail was received"""
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
        words = word[2]
        count[words] = count.get(words, 0) + 1
print(count)


# user_input = input('Enter filename: ')
# fhand = open(user_input)
# for line in fhand:
#    line = line.rstrip()
#    if not line.startswith('From '): continue
#    words = line.split()
#    print(words)
#    print(words[2])