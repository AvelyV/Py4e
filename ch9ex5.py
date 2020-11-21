d = dict()

try:
    file = input('Enter file name: ')
except:
    print('No file found')
    exit()

handle = open(file)

for line in handle:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0 or words[0] != 'From' : continue
    email = words[1]
    domain = email.split('@')
    #print(domain[1])
    if domain[1] not in d:
        d[domain[1]] = 1
    else:
        d[domain[1]] += 1

print(d)
