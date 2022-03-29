import re
# x = 'My 2 favorite numbers are 19 and 423'
# # [0-9] indicates that the search pattern should include all digits between 0 and 9 in the reference string
# y = re.findall('[0-9]+', x)  # re.findall() is used to search for all search strings
# print(y)

# x = 'agct is the new data source code blah blah blah'
# y = re.findall('[agct]+', x)
# print(y)

"""Warning: Greedy Matching"""
# the repeat characters (* and +) will always search and return the largest/longest search item
# based on the stamp/query search.
# x = 'From: Using the : character'
# this doesn't print out only the 'From:' that we want. It prints out 'From:' to last ':' which is not what we want
# y = re.findall('^F.+:', x)  # greedy matching
# print(y)

"""Suppressing Greedy Matching: Non-Greedy Matching"""
# x = 'From: Using the : character'
# the '?' character suppresses the greedy matching behavior and prints out the shorter version (the result we want) of
# search term
# y = re.findall('^F.+?:', x)
# print(y)

"""Fine-Tuning String Extraction"""
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# the '\S+@\S+' tells our program to search for the '@' in the string and do greedy-matching in a backwards-forwards
# manner, returning all the string containing that search item to us.
y = re.findall('\S+@\S+', x)
print(y)

"""Fine-tuning String Extraction using Parenthesis"""
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# using parenthesis tells our search term where to begin in the string and where to end
y = re.findall('^From (\S+@\S+)', x)  # this searches for any text starting with 'From' and containing the '@' and
# returns the string result without the 'From' because of the parenthesis.
print(y)

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# searches through the variable s to find any and every @ after a non-whitespace item
lst = re.findall('\\S+@\\S+', s)
print(lst)