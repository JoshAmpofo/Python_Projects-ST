"""This program takes a score between 0.0 and 1.0 and
returns an appropriate grade for score inputted"""
try:
    grade = float(input('Enter your score: '))
    if grade < 0.6:
        print('Your score', grade, 'is F')
    elif 0.6 <= grade <= 0.7:
        print('Your score', grade, 'is D')
    elif 0.7 <= grade <= 0.8:
        print('Your score', grade, 'is C')
    elif 0.8 <= grade <= 0.9:
        print('Your score', grade, 'is B')
    elif 0.9 <= grade <= 1.0:
        print('Your score', grade, 'is A')
    elif grade > 1.0:
        print('Your score', grade, 'is out of range')
except:
    print('Bad score')