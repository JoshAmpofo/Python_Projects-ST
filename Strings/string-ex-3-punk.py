"""This program contains a line that pranks users when a specific phrase is inputted.
And also prints out the number of subject lines in a file"""
fname = input('Enter filename: ')
try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':
        print(fname.upper(), "TO YOU - You have been punk'd")  # Easter egg!
    else:
        print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('Your file:', fname, 'has %d subject lines' % count)
