"""This program counts the number of messages from each person in a mailbox using dictionaries and tuples"""

# file handling
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File does not exist:', fname)
    quit()

# read through each line, find the appropriate line and start counting mails
di_mail = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    line = line.split()
    mails = line[1]
    di_mail[mails] = di_mail.get(mails, 0) + 1

# tuple list creation
tmp = list()
for key, value in di_mail.items():
    new_tup = (value, key)
    tmp.append(new_tup)

# searching for and printing the address with the most mail messages
bigcount = None
bigmail = None
tmp_2 = sorted(tmp, reverse=True)

for value, key in tmp_2:
    if bigcount is None:
        bigmail = key
        bigcount = value
print(bigmail, bigcount)
