"""This program is extracts a line in a file, convert the line to numerical values
computes the total of these value and finds the average.
After averaging, the last average result is printed."""

fname = input('Enter filename: ')  # user input

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)  # to handle user error
    exit()  # quit program if user inputs wrong string

count = 0
total = 0

for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):  # search for lines that contain this text
        stringnum = float(line[20:26])  # extract the floating point string in line and convert to numerical value
        count = count + 1
        total = total + stringnum
        avg = total/count
print('Average spam confidence:', round(avg, 12))  # print average spam confidence
