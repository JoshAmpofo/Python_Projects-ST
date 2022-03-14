counts = {'chuck': 1, 'fred': 42, 'jan': 100}
# for key in counts:  # for loop to retrieve only keys in dict
#    print(key, counts[key])

for key, value in counts.items():  # for loop to retrieve both key and value in dict
    print(key, value)

# print(counts.keys())  # to retrieve the keys in a dictionary
# print(counts.values())  # to retrieve the values in a dictionary
# print(counts.items())  # to retrieve all both keys and values in a dictionary
