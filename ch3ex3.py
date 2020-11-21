score = input('Enter score: ')
score = float(score)

if score > 1.0:
    print('Bad score')

if score >= 0.9:
    print('A')

if score >= 0.8:
    print('B')

if score >= 0.7:
    print('C')

if score >= 0.6:
    print('D')

if 0.0 > score < 0.6:
    print('F')

if score < 0.0:
    print('Bad score')
