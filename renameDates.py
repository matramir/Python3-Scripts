#! python3
# renameDates.py - Renames filenames  with American mm-dd-yyyy date format to european dd-mm-yyyy
# usage: renameDates.py <directory location>

import sys, os, shutil, re

if len(sys.argv) != 2:
    print('Please enter the directory path when calling the script.')
    print('python3 renameDates.py <directory path>')
    exit()
dirPath = sys.argv[1]
isDir = os.path.isdir(dirPath)
if isDir == False:
    print('Please enter an existing directory path.')
    exit()
else:
    #create a regex that matches files with the American date format
    datePattern = re.compile(r"""^(.*?) # all text before date
    ((0|1)?\d)-         # month digits from 01 or 1 to 12
    ((0|1|2|3)?\d)-     # day digits from 01 or 1 to 31
    ((19|20)?\d\d)      # year digits
    (.*?)$
    """, re.VERBOSE)

    #loop over the files in the dirPath
    for amerFilename in os.listdir(dirPath):
        mo = datePattern.search(amerFilename)

        #skip file without american style date
        if mo == None:
            continue

        #get the different parts of the filename
        beforePart = mo.group(1)
        monthPart = mo.group(2)
        dayPart = mo.group(4)
        yearPart = mo.group(6)
        afterPart = mo.group(8)

        #form european style filename
        euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

        #get full absolute filepath
        absWorkingDir = os.path.abspath(dirPath)
        ameriFilename = os.path.join(absWorkingDir, amerFilename)
        euroFilename = os.path.join(absWorkingDir, euroFilename)

        #Rename the filenames
        print('Renaming %s to %s ...' %(ameriFilename, euroFilename))
        shutil.move(ameriFilename, euroFilename)
