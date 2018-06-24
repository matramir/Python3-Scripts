# python3
# amazon.py - simple script that retrieves the item price from an amazon website
# usage: python3 amazon.py <url address>
import bs4, requests, sys
def getAmazonPrice (productUrl):
    res = requests.get(productUrl , headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"})
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems=soup.select('#newOfferAccordionRow > div > div.a-accordion-row-a11y > a > h5 > div > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')
    return elems[0].text.strip()
try:
    price = getAmazonPrice(sys.argv[1])
    print('The price is '+ price)
except:
    print("Something went wrong, please submit a valid url.")
