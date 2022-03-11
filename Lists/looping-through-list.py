"""This program will continue looping through a list of numbers from user until 'done' is inputted
and, it will then print out the average"""

"""Alternative 1 NB: uses less memory!!!"""
count = 0
total = 0

# while True:
#    user_input = input('Enter a number: ')
#    if user_input == 'done':
#        break
#    count = count + 1
#    try:
#        total = total + float(user_input)
#    except:
#        print('Not a valid number!')
#        continue
#    average = total/count
# print('Average:', average)

"""Alternative 2: using list methods NB: uses more memory!!!"""
num_list = list()
while True:
    user_input = input('Enter a number: ')
    if user_input == 'done':
        break
    try:
        user_num = float(user_input)
    except:
        print('Enter a valid number!')
        continue
    num_list.append(user_num)

average = sum(num_list)/len(num_list)
print('Average:', average)
