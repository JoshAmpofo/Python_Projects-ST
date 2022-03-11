"""This program goes through a file and searches for unique words, sorts them and adds to a new list"""

unique_words = []  # our empty list
fname = input('Enter a file: ')  # take file name from user
try:
    fhand = open(fname)
except:
    print('File does not exist!')
    quit()  # program should exit if wrong input/file name is made
for line in fhand:
    line = line.rstrip()
    elem = line.split()
    for item in elem:  # iterate through file and append word into new list if word not in new list
        if item not in unique_words:
            unique_words.append(item)
print(sorted(unique_words))  # return our new list with items in alphabetical order

