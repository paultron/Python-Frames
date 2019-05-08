import os
import sys
import fileinput

#matches = 0
oldList = []
newList = []

#print ("File to perform Search-Replace on:")
#fileToSearch  = input( "> " )

fileToSearch = 'C:\PyCUE\Profile-Blank.cueprofile'

#tempFile = open( fileToSearch, 'r+' )

with open(fileToSearch,'r+') as f:
    for line in f:
        for word in line.split():
            if word.startswith('<id>2'):
               oldList.append(int(word[4:14]))
               print('Old list: ' + str(oldList) + '\n')
               print('\n  matches: ' + str(len(oldList)) + '\n')
f.close()
