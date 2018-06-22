# python3
# andy.py - script that allows character battle log registration for D&D characters
# usage: creates a .txt file with a character name
import re, os, sys, datetime

#battle log regex
battleLogR = re.compile(r'''(
([A-Z][a-z\']+)           # charactername
(\s-\s)                   # spacer
([A-Za-z\s\.\-\,\"\'0-9]+)   # log content
)''',re.VERBOSE)

#ask for the battlelog
while(True):
    print('Enter a battle log with the format: \"CharacterName - Battle log contents\" to exit Enter: \"exit\"')

    log = input()
    if log == 'exit':
        exit()
    else:
        try:
            ls = battleLogR.search(log)

            characterName = ls.group(2)
            logContent = ls.group(4)

            print (characterName + ' does the following: '+ logContent)

            fileName = characterName + ".txt"
            charFilePath = os.path.join(os.path.abspath('.'),fileName)
            charFile = open(charFilePath, 'a')
            charFile.write("\n" + str(datetime.datetime.now()) + " - " + logContent)
            print('Log registered in:'+ charFilePath)
            charFile.close()
        except:
            print('Something went wrong, please try again')
            continue
