file = open('new.txt', 'w')  # careful as write(w) deletes all data from existing file
# or creates a new file if file doesn't exist!
print(file)

line1 = "Using this to test my python's file writing capability, \n"
print(file.write(line1))

line2 = "This is a new line i wrote into text file using python's \n" \
        "write method!"
print(file.write(line2))

file.close()  # this closes the file

fhand = open('new.txt')
for line in fhand:
    fhand = fhand.read()
print(fhand)
