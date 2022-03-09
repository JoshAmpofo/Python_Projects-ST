#hour = int(input('enter hours: '))
#rate = float(input('enter rate: '))

#base_pay = float(hour * rate)
#print('Your pay is $', round(base_pay, 2))

#cranking it up
try:
    hour = int(input('enter hours: '))
    rate = float(input('enter rate: '))

    if hour > 40:
        base_pay_reg = float(hour * rate)
        base_pay_ot = float(hour - 40.0) * float(rate * 0.5)
        base_pay_ot = base_pay_reg + base_pay_ot
        print('Your overtime pay is $', round(base_pay_ot, 2))
    else:
        base_pay_reg = float(hour * rate)
        print('Your regular pay is $', round(base_pay_reg, 2))
except:
    print('Please enter a numeric input!')
