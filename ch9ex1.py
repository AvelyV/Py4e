try:
    file = input('Enter file name: ')
    fhandel = open(file)
except:
    print('File not found')
    exit()

d = dict()   #create empty dictionary named d

for line in fhandel:        #loop through lines in fhandle
    line = line.rstrip()    #strip empty space on a right side of a line
    words = line.split()    #split line into words
    if len(words) == 0 : continue   #if no words on a line, continue
    for word in words:
        d[word] = d.get(word, 0) #add every word to dictionary d,
                                 #set zero as value
print(d)
