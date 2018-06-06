'''This File copy the content of Fileanswer1.txt to Fileanswer3.txt

The file whhich ive provided in the Github repository are the original Files .You can compile this program and
it can copy the copy the contenet of Fileanswer1 to Fileanswer3'''

from shutil import copyfile
copyfile('Fileanswer1.txt', 'Fileanswer3.txt')
#copyfile(source,Destination)