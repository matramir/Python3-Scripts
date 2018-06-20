#this script asks the user for a directory path and calculates the filesize of the files contained in the directory
#does not scan directories inside, only the first level files of the directory entered
import os
isPath = False
while (isPath == False) :
    print('Please write the path for the directory you want to know its total filesize:')
    path = input()
    isPath = os.path.isdir(path)
totalSize=0
for fileName in os.listdir(path):
    currentFile = os.path.join(path, fileName)
    if not os.path.isfile(currentFile) :
        continue
    totalSize += os.path.getsize(currentFile)
print ('Total Size: 'str(totalSize))
