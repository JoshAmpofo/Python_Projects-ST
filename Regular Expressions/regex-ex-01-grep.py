"""This program takes an input from the user in the form of a
regular expression and searches through the file, counting the times that string sequence appears
and prints out the total number of counts"""

import re  # regex module
user_input = input('Enter a regular expression: ')
fhand = open('mbox.txt')  # file handling
count = 0
for line in fhand:
    line = line.rstrip()
    # regex syntax
    if re.search(user_input, line):
        count = count + 1  # counter increases should search item be found
print('mbox.txt had', count, 'lines that matched', user_input)
