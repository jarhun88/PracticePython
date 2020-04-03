import os
import shutil

lis = []
i=1;

#name of folder that all other files will be put inside.
newFolder = '/Users/johnsong/Desktop/Cleanup'

while os.path.exists(newFolder):
    newFolder+=str(i)
    i+=1

#creating the folder     
os.makedirs(newFolder)

#adding every file/folder in desktop into newFolder Except for this file.
lis = os.listdir('/Users/johnsong/Desktop/')
for x in lis:
    print(x)
    if x=='cleanup.py':
        print("FILE REACHED")
        continue
    shutil.move(x,newFolder)
