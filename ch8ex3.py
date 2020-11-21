fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    if line == '' :
        continue
    words = line.split()
    #print('Debug: ',words)
    if len(words) < 1 or words[0] != 'From' : continue
    print(words[2])


#NOT SURE WHY NOT WORKING
#did not word bc I has 'From ' not 'From'
