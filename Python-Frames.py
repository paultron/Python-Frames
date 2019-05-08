import os
import sys
import fileinput

start = open('C:\DEV\Python-Frames\start.txt', 'r')
start1 = start.read()
start.close()

mida = open('C:\DEV\Python-Frames\mid-1st.txt', 'r')
mid1 = mida.read()
#mida.close()

midb = open('C:\DEV\Python-Frames\mid-2nd.txt', 'r')
#mid1 = midb.read()
#midb.close()

end = open('C:\DEV\Python-Frames\end.txt', 'r')
end1 = end.read()
end.close()

frames = 10

duration = 1000

color = '#ffffffff'

#open fresh .cueprofile
new = open('C:\DEV\Python-Frames\profilenew.cueprofile', 'w+')
#write beginning of file, unchanged, erasing it if it has contents
new.write(start1)
#change to append mode
new = open('C:\DEV\Python-Frames\profilenew.cueprofile', 'a')
# write the code for inserting the frames
oldNum = 660
new.write('\n' + mid1 + '\n')
for fr in range(frames-1):
    if oldNum == 660:
        new.write(('\t'*23) + '<value' + str(fr +1) + '>\n')
    else:
        new.write('\n' + ('\t'*23) + '<value' + str(fr +1) + '>\n')
    
    midb = open('C:\DEV\Python-Frames\mid-2nd.txt', 'r')
    with midb as f:
        flip = True
        for line in f:
            if '<id>21' in line:
                nid = list(line)
                nid[-9:-6] = list(str(oldNum))
                new.write(''.join(nid))
                oldNum += 1
            else:
                new.write(line)

    new.write('\n' + ('\t'*23) + '</value' + str(fr +1) + '>')
###append the rest of the profile
###adjusting the <id> numbers along the way
new.write('\n' + end1)

#close the file
new.close()
