#make a function to count the number of letters 'a' in an input

def count(y):
    counter = 0
    for letter in y:
        if letter == 'a':
            counter = counter + 1
    return counter

text = input('Enter text: ')
x = count(text)
print(x)
