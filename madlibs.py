# python3
# madlibs.py - This script allows you to play madlibs with a .txt file
# usage: the .txt file should contain a sentence with the words "ADJECTIVE, NOUN, ADVERB OR VERB"
import re, os

#asks for a existing file
fileExists = False
fileExtension = ''
filePath = ''
dirExists = False
while ((fileExists == False)) :
    print('Please enter the file path of the .txt message you want to play madlibs with:')
    filePath = input()
    fileExists = os.path.exists(filePath)
#open file
madLibs = open(filePath)
#save the contents of the file
content = madLibs.read()
madLibs.close()
#regex definition to find any of the keywords for madLibs
check = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
#loop to check if there are words to replace:
while True:
    result = check.search(content)
    if result == None:
        break
    print ('Please enter a %s:' % (result.group().lower()))
    i = input()
    content = check.sub(i,content,1)
#after replacing all the keywords it displays the resulting sentence
print ('Result: '+ content)
#asks if the user wants to print the resulting file in a madLibs_Result file output
print('Do you want to print the resulting file?\n(yes/no)')
answer = input()
if answer == 'yes' :
    while dirExists == False:
        print('Please enter the directory of the resul file:/n(Write cancel to exit.)')
        resultPath = input()
        if resultPath == 'cancel' :
            break
        else:
            dirExists = os.path.isdir(resultPath)
            if dirExists == True:
                resultFile = open(os.path.join(resultPath, 'madLibs_Result.txt',"w"))
                resultFile.write(content)

exit()
