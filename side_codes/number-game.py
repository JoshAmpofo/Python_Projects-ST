print('*** Welcome to the guess a number game!. Guess the right number between 1 and 10 to win ***')

count = 0
while True:
    user_inp = input('Enter a number: ')
    try:
        user_num = int(user_inp)
        if user_num == 3:
            print('Hurray!!! You guessed right!')
            break
        elif 1 <= user_num <= 2:
            print('So close but no cigar')
        elif 4 <= user_num <= 10:
            print('Way off the bat!')
    except:
        print('Try again')
        continue
    count = count + 1
    if count == 3:
        print('Total tries up:', count)
        print('Game Over!')
        quit()
