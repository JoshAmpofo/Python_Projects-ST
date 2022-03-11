"""This program takes a list of numbers from a user and prints the minimum and maximum numbers at end of run"""
numlist = list()
while True:
    user_input = input('Enter a number: ')
    if user_input == 'done':
        break
    try:
        user_num = float(user_input)
    except:
        print('Enter a valid number!')
        continue
    numlist.append(user_num)

max_num = max(numlist)
min_num = min(numlist)
print('Maximum: ', max_num)
print('Minimum: ', min_num)
