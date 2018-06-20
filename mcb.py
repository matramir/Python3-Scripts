#! python3
# mcb.py saves and loads pieces of text to the clipboard
# usage: mcb.py save <keyword> - saves clipboard to keyword
#        mcb.py <keyword> - loads keyword to clipboard
#        mcb.py list - loads all keywords to clipboard

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')
# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2 :
    #list keywords and load content
    if sys.argv[1].lower() == 'list' :
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
else:
    print('Wrong command. Please cat the script for more information regarding proper usage.')

mcbShelf.close()
