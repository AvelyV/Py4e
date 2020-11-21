hours = input('Enter hours: ')
rate = input('Enter rate: ')

try:
    pay = int(hours) * int(rate)
    print('Pay', pay)

except:
    print('Error, please enter numeric value')
