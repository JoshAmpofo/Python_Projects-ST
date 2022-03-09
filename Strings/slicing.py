# s = 'Monty Python'
# print(s[0:4])
# print(s[6:7])
# print(s[6:20])
# print(s[:])
# a = 'hello'
# b = a + ' There'
# print(b)

# String Comparison
# word = 'banana'
# if word == 'banana':
#    print('All right, bananas')

# if word < 'banana':
#    print('Your word,' + word + ', comes before banana')
# elif word > 'banana':
#    print('Your word,' + word + ', comes after banana')
# else:
#    print('All right, bananas.')

# String Library
# greet = 'Hello Bob'
# zap = greet.lower()
# print(zap)

# print('Hi There'.lower())

# print(type(greet))
# print(dir(greet))
# word = greet.find('ell')
# print(word)

# word = 'bananana'
# i = word.find('na')
# print(i)

word = 'banana'
# new_word = word.upper()
# print(new_word)
print(word.count('a'))  # using the .count() method

camels = 42
# print('%d' % camels)  # %d stands for format decimal
# print('I have spotted %d camels.' % camels)
print('In %d years, I have spotted %g %s.' % (3, 0.1, 'camels'))  # %g stands for floating points, %s stands for strings

