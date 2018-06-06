with open('Fileanswer1.txt') as fh1, open('Fileanswer3.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        print(line1 + line2)
