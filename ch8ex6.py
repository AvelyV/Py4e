#Ask user for numbers until 'done' is entered. Store numbers in a list and
#calculate min and max

numbers = list()

while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numbers.append(value)


x = max(numbers)
z = min(numbers)

print('Maximum: ', x)
print('Minimum: ', z)
