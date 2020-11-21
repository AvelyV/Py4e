fname = input("Enter file name: ")
fh = open(fname)
lst = list()

#
for line in fh:
    line.rstrip()
    #create list of words, named words, that were in a line
    words = line.split()

    #loop through the words in the list 'words'
    for word in words :
        #if word is in the list called lst, continue
        if word in lst:
            continue
        #If word is not on lst, add it
        lst.append(word)
    #print('LIST: ', words)

    lst.sort()
print(lst)
