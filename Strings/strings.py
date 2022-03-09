# fruit = 'banana'
# for letter in fruit:  # always use a for loop when iterating through strings
#    print(letter)  # it's more elegant that way
#  letter = fruit[1]
#  print(letter)

#  print(len(fruit))

#  index = 0
#  while index < len(fruit):
#    letter = fruit[index]
#    print(index, letter)
#    index = index + 1

# Looping and counting
# word = 'banana'
# count = 0

# for letter in word:
#    if letter == 'a':
#        count = count + 1
# print(count)

# word = 'banana'
# index = 0
# while index < len(word):
#    letter = word[index - 1]
#    index = index-1
#    print(letter)  # while loop gives correct output but throws an error

# Search and Replace
# dna = 'AGCTTCGGACCAA'
# rna = dna.replace('T', 'U')
# print(rna)

# Stripping Whitespace
# dna = ' AGCT '
# print(dna)
# print(dna.lstrip())  # lstrip() removes whitespace to the left of string
# print(dna.rstrip())  # rstrip() removes whitespace to the right
# print(dna.strip())  # strip() removes whitespaces in the beginning and end of string

# Prefixes
# sentence = 'This is a big sequence'
# print(sentence.startswith('This'))
# print(sentence.startswith('h'))

# Parsing and Extracting
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# finding email from string
atpos = data.find('@')  # gives index position of @ sign
print(atpos)

spos = data.find(' ', atpos)  # gives index position of the next space after the @ sign
print(spos)

email = data[atpos+1:spos]  # to find email, increase index of @ sign and splice string up to space after @ sign
print(email)

# finding sender ID
name = data.find('stephen')
print(name)

atpos = data.find('@')
print(atpos)

email_ID = data[name:atpos]
print(email_ID)