"""while loops, also known as indefinite loops"""

# n = 5
# while n > 0:
#    print(n)
#    n = n - 1
# print('Blastoff')
# print(n)

# breaking out of loops
# while True:
#    line = input('> ')
#    if line == 'done':
#        break #ends loop and jumps to the end of the code
#    print(line)
# print('Done!')

# while True:
#    line = input('> ')
#    if line == '#':
#        continue
#    if line == 'done':
#        break
#    print(line)
# print('Done!!!')


# """For loop, also known as definite Loops"""

#"""This code finds the largest value in a list and returns it"""
#largest_num_so_far = -1  # set an initial variable to hold largest num value
#print('largest number before loop', largest_num_so_far)
#for number in [3, 41, 12, 9, 74, 15]:
#    if number > largest_num_so_far:
#        largest_num_so_far = number
#    print('largest number so far is', largest_num_so_far)

#print('After iteration, largest number is:', largest_num_so_far)

"""This code find the smallest value in a list of numbers"""
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)
