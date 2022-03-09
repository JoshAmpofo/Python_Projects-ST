"""This code searches the largest value in a list"""
largest_so_far = None
print('Largest number so far is:', largest_so_far)

for number in [9, 41, 12, 3, 74, 15]:
    if largest_so_far is None or number > largest_so_far:
        largest_so_far = number
    print(largest_so_far, number)
print('largest number is:', largest_so_far)