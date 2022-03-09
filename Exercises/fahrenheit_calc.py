"""This program takes temperature input from users in celsius and converts it to fahrenheit"""
temp = input('Enter temperature (celsius): ')
try:
    fahr = int(temp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a valid temp in integers')

pass

