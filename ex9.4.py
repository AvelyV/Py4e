# Write a program to read through the mbox-short.txt and figure out who has
# sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines
# as the person who sent the mail. The program creates a Python dictionary
# that maps the sender's mail address to a count of the number of times they
# appear in the file. After the dictionary is produced, the program reads
# through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
maxaddress = " "
maximum = 0

for line in handle:                   #separate file into lines
    line = line.rstrip()
    words = line.split()              #split line into words
    # print('WORDS: ', words)
    # print('LINEs: ', line)
    if len(words) == 0 : continue      #skip empty lines
    if words[0] != "From" : continue  #skip lines that don't start with "From"
    # print('Words: ', words)
    if words[1] not in counts:
        counts[words[1]] = 1      # First entry
    else:
        counts[words[1]] += 1     # Additional counts

# print('Dictionary: ',counts)


for address, count in counts.items():
    if maximum is None or count > maximum :
        maximum = count
        maxaddress = address


print(maxaddress, maximum)
