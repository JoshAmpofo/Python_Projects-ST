# fhand = open('mbox-short.txt')
# for line in fhand:
#    line = line.rstrip()  # removes the whitespace between emails
    # Skip uninteresting lines
#    if not line.startswith('From: '):  # searches for lines starting with 'From'
#        continue
#    print(line)

# Using in to skip unwanted output

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:  # use this method to filter output
        continue
    print(line)
