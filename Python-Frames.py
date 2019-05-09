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

times = 0
oldNum = 660 #<id> counter
fps = 3
duration = 1000 #in ms, 1sec = 1000
colors = ['BFEFFF', '00CED1', '40E0D0'] 

frames = (int(duration/1000) * fps) #fits actual frames to length

colorList = []
for i in range(frames+2):
    for c in range(len(colors)):
        colorList.append(colors[c])

#open fresh .cueprofile
new = open('C:\DEV\Python-Frames\profilenew.cueprofile', 'w+')
#write beginning of file, unchanged, erasing it if it has contents
new.write(start1)
#change to append mode
new = open('C:\DEV\Python-Frames\profilenew.cueprofile', 'a')
# write the code for inserting the frames

for fr in range(1,frames+1):
    for col in range(len(colors)):
        if col == 0 and fr == 1:
            mida = open('C:\DEV\Python-Frames\mid-1st.txt', 'r')
            with mida as f:
                new.write('\n')
                for line in f:
                    if '<time>' in line:
                        new.write(('\t'*32) + '<time>' + str(times/frames) + '</time>\n')
                        times += 1
                    elif '<duration>' in line:
                        new.write(('\t'*31) + '<duration>' + str(duration) + '</duration>\n')
                    elif '<color>' in line:
                        new.write(('\t'*32) + '<color>#FF' + colorList[0] + '</color>\n')
                    else:
                        new.write(line)
                new.write('\n')
        else:       
            times = 0
            midb = open('C:\DEV\Python-Frames\mid-2nd.txt', 'r')        
            with midb as f:
                if oldNum == 660:
                    new.write(('\t'*23) + '<value' + str(fr) + '>\n')
                    #omits the newline for the first new frame
                    
                else:
                    new.write('\n' + ('\t'*23) + '<value' + str(fr) + '>\n')
                print('\nframe: ' + str(fr)
                      + '\ncol: ' + str(col)
                      )

                for line in f:
                    if '<id>21' in line:
                        nid = list(line)
                        nid[-9:-6] = list(str(oldNum))
                        new.write(''.join(nid))
                        oldNum += 1
                        
                    elif '<duration>' in line:
                        new.write(('\t'*31) + '<duration>' + str(duration) + '</duration>\n')
                        
                    elif '<time>' in line:
                        new.write(('\t'*32) + '<time>' + str((fr-1+times)/frames) + '</time>\n')
                        times += 1
                        
                    elif '<color>' in line:
                        new.write(('\t'*32) + '<color>#FF' + colorList[col] + '</color>\n')
                        print(colorList[col])
                        
                    else:
                        new.write(line)

                new.write('\n' + ('\t'*23) + '</value' + str(fr) + '>')
        
###append the rest of the profile
new.write('\n' + end1)

#close the file
mida.close()
midb.close()
new.close()
