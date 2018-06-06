'''
In this scernerio our File name is "Fileanswer1.txt"
'''

def LastNLines(f,n):
    with open(f) as file:
        print('Last ',n,'Lines from File:',f)
        for line in (file.readlines()[-n:]):
            print(line,end='')

name=input('Enter the File name:')
n=int(input('No.of last Lines to be Read:'))
try:
    LastNLines(name,n)
except:
    print('File Error')