"""This program demonstrates use of guardian code"""
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
#    print('Debug:', words)
# rewrote code into a compound logical expression
    if len(words) == 0 or words[0] != 'From': continue  # Guardian code (saves the program from crashing)
#    if words[0] != 'From': continue
    print(words[6])
