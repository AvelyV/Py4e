text = input('Text here: ')

lenght = len(text)
print('Lenght: ', lenght)

index = lenght - 1

#while index < len(text):
while 0 <= index <= (len(text)-1):
    letter = text[index]
    print(letter)
    index = index -1
