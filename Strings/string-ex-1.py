"""This program reads through a file and prints the count of the file
line by line and in uppercase"""

fname = input('Enter filename: ')  # user input

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)  # to handle user error
    exit()  # quit program if user inputs wrong string

for line in fhand:
    line = line.rstrip()
    line = line.upper()  # convert each line to uppercase
    print(line)  # output uppercase lines
