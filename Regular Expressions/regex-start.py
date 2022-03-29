"""to use regular expressions, you first have to import the module 're'
you can use 're.search()' to see if a string matches a regular expression
this is similar to using the 'find()' method for strings.
You can use 're.findall()' to extract portions of a string that match your
 regular expression, similar to a combo of find() and slicing: var[5:10]"""

import re

"""Using re.search() like find () to search for items"""
# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if re.search('From:', line):
#         print(line)

"""Using re.search() like startswith()"""

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if re.search('^From:', line):  # fine-tune matching by adding special characters to the string
#         print(line)

"""Using wild-card characters"""
# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if re.search('^X.*:', line):  # wild card '.*'
#         print(line)

"""Fine tuning wild card character search"""
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if re.search('^X-\S+:', line):  # wild card '-\S' signifies matching any non-whitespace char
        print(line)
