# python3
# mapit.py - opens a browser page with the google maps page that shows the street address
# usage: mapit <street address> or mapit clipboard
# for windows is recommended to create a batch file so you can call the function more easily
import webbrowser,sys, pyperclip


if len(sys.argv) > 1:
    address=''
    if sys.argv[1] == 'clipboard':
        address =pyperclip.paste()
    else:
        address = '+'.join(sys.argv[1:])
    webbrowser.open('https://www.google.com/maps/place/'+address+'/')
else:
    print('Please use the command as the following: mapit <street address> or mapit clipboard')
