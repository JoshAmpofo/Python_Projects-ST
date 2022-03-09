"""This program reads numbers inputted by a user repeatedly
until the user enter done and program stops!"""

count = 0
tot = 0.0

while True:
    value = input('Enter a number: ')
    if value == 'done':
        break
    try:
        float_value = float(value)
    except:
        print('Invalid Input!')
        continue
    count = count + 1
    tot = tot + float_value
print(count, tot, tot / count)
