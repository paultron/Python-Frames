import os
import sys
import fileinput

start = open('C:\DEV\PyCUE\start.txt', 'r')
start1 = start.read()
start.close()
mid = open('C:\DEV\PyCUE\mid.txt', 'r')
mid1 = mid.read()
mid.close()
end = open('C:\DEV\PyCUE\end.txt', 'r')
end1 = end.read()
end.close()


#open fresh .cueprofile
new = open('C:\DEV\PyCUE\profilenew.cueprofile', 'w+')
#write beginning of file, unchanged
new.write(start1)
#change to append mode
new = open('C:\DEV\PyCUE\profilenew.cueprofile', 'a')
##### write the code for inserting the frames
new.write('\n' + mid1)

#append the rest of the profile, adjusting the <id> numbers along the way
new.write('\n' + end1)



#close the file
new.close()
