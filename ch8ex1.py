#Write a function called chop that takes a list and modifies it,
#removing the first and the last elements, and return None.
#Then write a function called middle that takes a list and returns a new list
#that contains all but  the first and the last elements.

def chop(list):
#list = [1, 2, 3, 4, 'a', '14']
    #delete first element
    del list[0]
    #delete last element
    del list[len(list) -1]
    #print(list)


def middle(list):
    new = list[1:]
    del new[len(new) -1]
    return new

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = ['a', 'v', 'e', 'l', 'y']

choplist = chop(list1)
print(list1)
print(choplist)

middlelist = middle(list2)
print(list2)
print(middlelist)
