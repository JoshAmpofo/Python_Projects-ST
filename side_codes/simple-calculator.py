while True:
    try:
        user_num_1 = float(input('Enter your 1st number: '))
        user_num_2 = float(input('Enter your 2nd number: '))
    except:
        print('Enter a numerical value!')
        continue
    
    option = input('choose operation:\n''add\n' 'subtract\n''divide\n''multiply\n \n')

    add = user_num_1 + user_num_2
    subtract = user_num_1 - user_num_2
    multiply = user_num_1 * user_num_2
    divide = user_num_1 / user_num_2

    if option == 'add':
        print('Your operation: ', user_num_1, ' + ', user_num_2, '= ', add)

    elif option == 'subtract':
        print('Your operation: ', user_num_1, ' - ', user_num_2, '= ', subtract)

    elif option == 'divide':
        print('Your operation: ', user_num_1, ' / ', user_num_2, '= ', divide)

    elif option == 'multiply':
        print('Your operation: ', user_num_1, ' x ', user_num_2, '= ', multiply)
    quit()
