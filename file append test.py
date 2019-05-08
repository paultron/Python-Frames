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

new = open('C:\DEV\PyCUE\profilenew.cueprofile', 'w+')
new.write(start1)
new = open('C:\DEV\PyCUE\profilenew.cueprofile', 'a')
new.write('\n' + mid1)
new.write('\n' + end1)
new.close()

