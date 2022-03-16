def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


user_num_1 = float(input('Enter first number: '))
user_num_2 = float(input('Enter second number: '))

print('Select operation: ')
print('1. Add'), print('2. Subtract'), print('3. Multiply'), print('4. Divide')

choice = input('Select your choice(1, 2, 3, 4): ')

if choice == '1':
    print(user_num_1, '+', user_num_2, '=', add(user_num_1, user_num_2))
elif choice == '2':
    print(user_num_1, '-', user_num_2, '=', subtract(user_num_1, user_num_2))
elif choice == '3':
    print(user_num_1, 'x', user_num_2, '=', multiply(user_num_1, user_num_2))
elif choice == '4':
    print(user_num_1, '/', user_num_2, '=', divide(user_num_1, user_num_2))
else:
    print('Invalid input')
quit()
