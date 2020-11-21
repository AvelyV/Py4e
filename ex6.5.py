text = "X-DSPAM-Confidence:   0.8475";

bpos = text.find(':')
#print(bpos)

number = text[bpos+1:]

value = float(number)
print(value)
