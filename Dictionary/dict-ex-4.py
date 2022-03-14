"""This program searches through a mail log and finds out which mail has
the most messages"""
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

message_num = None
email = None
for sender, count in count.items():
    if message_num is None or count > message_num:
        email = sender
        message_num = count

print(email, message_num)
