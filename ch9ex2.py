d = dict()
maxday = None
maximum = None

try:
    file = input('Enter file name: ')
except:
    print('File not found')
    exit()

fhandle = open(file)

for line in fhandle:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0 or words[0] != 'From' : continue
    if words[2] not in d:
        d[words[2]] = 1
    else:
        d[words[2]] += 1

print(d)

for k, v in d.items():
    if maximum is None or v > maximum:
        maximum = v
        maxday = k

print(maxday, maximum)
