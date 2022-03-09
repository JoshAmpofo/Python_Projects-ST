"""This program searches for the smallest value in a list of number"""
smallest_so_far = None
print('Smallest value so far: ', smallest_so_far)
for values in [9, 41, 12, 3, 74, 15]:
    if smallest_so_far is None:
        smallest_so_far = values
    elif values < smallest_so_far:
        smallest_so_far = values
    print(smallest_so_far, values)
print('smallest value is: ', smallest_so_far)