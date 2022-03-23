"""This program reads through a file and counts the frequency of hours an email was received"""

# File handling
fname = input('Enter a filename: ')
try:
    fhand = open(fname)
except:
    print('File does not exist:', fname)
    quit()

# read through each line, find the appropriate line and start counting number of hours
count = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    line = line.split()
    time = line[5]

    time_split_first = time.split(':')
    time_split_hour = time_split_first[0]
    count[time_split_hour] = count.get(time_split_hour, 0) + 1

# create tuple list
tmp = list()
for hour, count in count.items():
    new_tup = (hour, count)
    tmp.append(new_tup)

# return the hour and frequency
lst = sorted(tmp)
for key, value in lst:
    print(key, value)



