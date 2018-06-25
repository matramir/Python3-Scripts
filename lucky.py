# python3
# lucky.py - open several search results on a web browser
# usage: python3 lucky.py <search values>

import requests, sys, webbrowser, bs4

print('Googling...')#display while downloading the google plage
try:
    res = requests.get('http://google.com/search?q='+' '.join(sys.argv[1:]))
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    linkElems = soup.select('.r a')

    numOpen = min(5, len(linkElems))

    for i in range(numOpen):
        webbrowser.open('http://google.com' + linkElems[i].get('href'))
except:
    print('Something went wrong, please try again')
