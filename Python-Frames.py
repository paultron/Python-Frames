import os
import sys
import fileinput

start = open('C:\DEV\Python-Frames\start.txt', 'r')
start1 = start.read()
start.close()

#mida = open('C:\DEV\Python-Frames\mid-1st.txt', 'r')
#mid1 = mida.read()
#mida.close()

#midb = open('C:\DEV\Python-Frames\mid-2nd.txt', 'r')
#mid1 = midb.read()
#midb.close()

end = open('C:\DEV\Python-Frames\end.txt', 'r')
end1 = end.read()
end.close()

times = 0 #frame counter

oldNum = 660 #<id> counter

fps = 30

duration = 1000 #not implemented, in ms, 1sec = 1000

frames = int(duration/1000) * fps #fits frames to length

color = '#ffffffff' #not implemented

#open fresh .cueprofile
new = open('C:\DEV\Python-Frames\profilenew.cueprofile', 'w+')
#write beginning of file, unchanged, erasing it if it has contents
new.write(start1)
#change to append mode
new = open('C:\DEV\Python-Frames\profilenew.cueprofile', 'a')
# write the code for inserting the frames

mida = open('C:\DEV\Python-Frames\mid-1st.txt', 'r')
##new.write('\n' + mida + '\n')
with mida as f:
    new.write('\n')
    for line in f:
        if '<time>' in line:
            new.write(('\t'*32) + '<time>' + str(times/fps) + '</time>\n')
            times += 1
        else:
            new.write(line)
    new.write('\n')
    
for fr in range(frames-1):
    if oldNum == 660:
        new.write(('\t'*23) + '<value' + str(fr +1) + '>\n')
        #omits the newline for the first new frame
    else:
        new.write('\n' + ('\t'*23) + '<value' + str(fr +1) + '>\n')
        
    times -= 1 # ensures 0-1, 1-2, etc
    midb = open('C:\DEV\Python-Frames\mid-2nd.txt', 'r')
    with midb as f:
        for line in f:
            if '<id>21' in line:
                nid = list(line)
                nid[-9:-6] = list(str(oldNum))
                new.write(''.join(nid))
                oldNum += 1
            elif '<time>' in line:
                new.write(('\t'*32) + '<time>' + str(times/fps) + '</time>\n')
                times += 1                
            else:
                new.write(line)

    new.write('\n' + ('\t'*23) + '</value' + str(fr +1) + '>')
    
###append the rest of the profile
new.write('\n' + end1)

#close the file
mida.close()
midb.close()
new.close()
