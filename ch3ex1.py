#revrite your pay computations to give the employee 1.5 times
#the houerly rate for hoursworked above 40 hours.

hours = input("Enter hours: ")
rate = input('Enter rate: ')

try:
    hr = float(hours)
    rt = float(rate)

except:
    print('Please enter numeric input')
    quit()

print(hr, rt)
if hr > 40:
    reg = rt * hr
    otp = (hr - 40.00) * (rt * 0.5)
    xp = reg + otp
else:
    xp = hr * rt
print('Pay:', xp)
