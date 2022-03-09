"""We use open() to open files in python"""
# fhand = open('mbox.txt')
# print(fhand)  # if open successful, the OS returns a file handle

# newline character
# stuff = 'Hello\nworld!'
# print(stuff)
# print(len(stuff))

# Counting through a file
# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#    count = count + 1
# print('Line count:', count)

# Reading the whole/entire file
# Use the .read() method when the file contains info that can fit into memory
# However if the file is large, then use a for or while loop to read
# Program in bits.
# fhand = open('mbox-short.txt')
# inp = fhand.read()  # reads the entire file
# print(len(inp))
# print(inp[:20])

fhand = open('mbox-short.txt')
for line in fhand:
    print(line)
