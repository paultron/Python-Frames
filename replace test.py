import os
import sys
import fileinput

frames = 20

oldList = []
newList = []
#newWord = ''

oldF = open('C:\DEV\PyCUE\profile-5-copied.cueprofile', 'r+')
newF = open('C:\DEV\PyCUE\profile-xxx.cueprofile', 'w+')

with oldF as f:
    for line in f:
        if '<id>2147483' in line:
            #newList.append(line)
            s = list(line)
            print(s)
            s2 = s[-9:-6]
            
            print("".join(s2))
        #for word in line.split():
            #if word.startswith('<id>2'):
                #newWord = word[0:4] + 'xxx' + word[14:]
                
                #s = s[:index] + newstring + s[index + 1:]
##                oldList.append(int(word[4:14]))
##                if int(word[4:14]) > 2147483653: 
##                   newList.append(int(word[4:14]) + frames)
##                else:
##                    newList.append(int(word[4:14]))
##                    
##                print('Old list: ' + str(oldList) + '\n')
##    print('New list: ' + str(newList)+ '\n')
##                print('Matches: ' + str(len(oldList)) + '\n')
##                print('Changed: ' + str(len(newList)-5) + '\n')
        #newF.write(line)

oldF.close()
newF.close()
