#! python3
# trent.py - This simple script uses the os.walk function to show
# folders, subfolders and filenames in a given directory.
# usage: write trent,py <directory>

import sys, os
if len(sys.argv) != 2:
    print ('Please enter the filepath when calling the script as described in the script documentation')
    exit()
dirPath = sys.argv[1]
isDir = os.path.isdir(dirPath)
if isDir == False:
    print ('Please enter an existing directory.')
    exit()
else:
    for folderName, subfolders, filenames in os.walk(dirPath):
        print('The folder is '+folderName)
        print('The subfolders in '+ folderName+" are "+str(subfolders))
        print('The filenames in '+ folderName+' are '+str(filenames))
        print()
