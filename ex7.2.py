# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    #print(line)

    bpos = line.find(':')

    number = line[bpos+1:]

    value = float(number)

    count = count + 1

    total = total + value

    avarage = total /count


print('Average spam confidence:', avarage)
#print('Count: ', count)
#print("Done")
