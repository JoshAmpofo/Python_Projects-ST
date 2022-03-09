"""This program takes user input and returns mina and max values"""
empt_list = []  # to store input of user as list
count = 0  # initial count value
total = 0  # initial total value

while True:
    user = input('Enter a number: ')
    if user == 'done':
        break  # leave loop once correct keyword is mentioned
    try:
        user_num = int(user)
    except:
        print('Invalid input!')  # Error handling
        continue  # program should run even after error output
    for i in range(user_num):  # handles first and last input of user
        empt_list.append(user_num)  # add user input to empt_list
    count = count + 1
    total = total + user_num
print(count, total, min(empt_list), max(empt_list))  # print out desired output
