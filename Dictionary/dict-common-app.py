"""Counting the frequency of things is one of the most common
application of dictionaries"""
# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names:
#    if name not in counts:
#        counts[name] = 1  # counting new lines/elements in dict
#    else:
#        counts[name] = counts[name] + 1  # counting existing lines/elements in dict
# print(counts)


"""Simplifying counting with get()"""
# The get() method is used to find the item you want a value from.
# The default 0 is returned when the item does not exist in the dictionary
counts = dict()
name = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in name:
    # search through the dictionary and count the number of times an item appears
    counts[name] = counts.get(name, 0) + 1
print(counts)
