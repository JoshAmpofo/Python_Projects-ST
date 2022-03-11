"""This program searches through an email file and returns the sender email and date of sending """
user_input = input('Enter filename: ')
fhand = open(user_input)
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
#    print(words)
    print(words[1:5], words[6])

