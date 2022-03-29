import re
fhand = open('mbox-short.txt')
numlist = list()

for line in fhand:
    line = line.rstrip()
    numbers = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(numbers) != 1: continue
    print(numbers)
    num = float(numbers[0])
    numlist.append(num)
print('Maximum:', max(numlist))
