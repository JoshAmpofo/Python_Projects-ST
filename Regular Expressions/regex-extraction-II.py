import re
# line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# '@([^]*) means search for non-blank spaces starting from the @ string
# this method can be over greedy and print out other search terms we don't require
# line_extract = re.findall('@([^ ]*)', line)
# print(line_extract)

"""Even cooler regex version"""
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# this method makes it more precise in finding the search term and outputting the right result
# it says start from 'From' search through any non-block string and when you get to the '@'
# stop there, print out the search item we want and stop there '()'.
line_extract_2 = re.findall('^From .*@([^ ]*)', line)
print(line_extract_2)
