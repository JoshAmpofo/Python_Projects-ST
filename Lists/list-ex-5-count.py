fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: %s does not exist!' % fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        count = count + 1
        print(words[1])
print('There were %d lines in the file with From as the first word' % count)