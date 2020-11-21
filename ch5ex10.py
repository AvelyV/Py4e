largest = None
smallest = None

while True:

    sval = input("Enter a number: ")
    if sval == "done" :
        break
    try:
        num = int(sval)

    except:
        print('Invalid input')
        continue


    if largest is None:
        largest = num
    elif num > largest:
        largest = num

    if smallest is None or num < smallest:
        smallest = num

print("Maximum is", largest)
print('Minimum is', smallest)
