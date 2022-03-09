#x = 5
#if x > 2:
#    print('Bigger than 2')
#    print('Still bigger')
#print('Done with 2')

#for i in range(5):
#    print(i)
#    if i > 2:
#        print('Bigger than 2')
#    print('Done with i')
#print('All done!')

#ifelse statements
x = 9

#if x < 2:
#    print('Below 2')
#elif x < 20:
#    print('Below 20') #order of code matters. next line will never be executed no matter value of x
#elif x < 10:
#    print('Below 10')
#else:
#    print('Something else')

#tryexcept
rawstr = input('enter a number:')
try:
    eval = int(rawstr)
except:
    eval = -1

if eval > 0:
    print('Nice work!')
else:
    print('not a number!')