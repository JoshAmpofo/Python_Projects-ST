"""This program reads a file and prints the letters in decreasing order of frequency.
It doesn't count spaces, numerics and special characters!"""

# file handling
fname = input('Enter a file: ')
try:
    if len(fname) < 1: fname = 'clown.txt'
    fhand = open(fname)
except:
    print("File doesn't exist:", fname)
    quit()

# search through each line in file, remove spaces, read words and count letters
lst = dict()
for lin in fhand:
    line = lin.rstrip()
    for letters in line:
        if letters in 'abcdefghijklmnopqrstuvwxyz':
            lst[letters.lower()] = lst.get(letters.lower(), 0) + 1

# create tuple list to store dict.items()
tmp = list()
for key, value in lst.items():
    tmp.append((value, key))

# reverse order and return letters in decreasing order of frequency
tmp_2 = sorted(tmp, reverse=True)
for value, key in tmp_2:
    print(key, value)
