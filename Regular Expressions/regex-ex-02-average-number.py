"""This program searches through a user input file and searches for a particular sequence of numbers using regex
The numbers are then converted to integers and the average printed to screen"""
import re
# file handling
fname = input('Enter file: ')
try:
    fhand = open(fname)
except:
    print('Your file', fname, 'does not exist!')
    quit()

# set counters for average
count = 0
total = 0

# more file handling
for line in fhand:
    line = line.rstrip()
    # regex syntax
    numbers = re.findall('^New Revision: ([0-9]+)', line)
    if len(numbers) != 1: continue  # handle empty list
    num = int(numbers[0])  # retrieve first item in string list and convert to integer
    count += 1
    total = total + num
    avg = int(total/count)
print('The average of the numbers are:', avg)
