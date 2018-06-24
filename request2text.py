# python3
# requests2text.py - script that contains the request.get method and writing loop to a txtfile
# usage: python3 request2text.py <web address> <.txt file name>
#    or  python3 request2text.py clipboard <.txt file name>

import requests, pyperclip, sys, os

if len(sys.argv) != 3:
    print('Please use request2text.py as the following:request2text.py <web address> <.txt file name>')
    print('or python3 request2text.py clipboard <.txt file name>')
    exit()
else:
    address=''
    filename=''
    try:
        if (sys.argv[1] == 'clipboard'):
            address = pyperclip.paste()
        else:
            address=sys.argv[1]
        filename = sys.argv[2]+'.txt'
        filepath = os.path.join(os.path.abspath('.'),filename)
        res = requests.get(address)
        endfile=open(filepath, 'wb')
        for chunk in res.iter_content(10000):
            endfile.write(chunk)
        endfile.close()
        print('Webcontent from :'+address+'\n successfully written in: '+filepath)
        print(res.raise_for_status)

    except:
        print('Something went wrong, please revise your command and try again')
        exit()
