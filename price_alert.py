from requests import get
from contextlib import closing
from bs4 import BeautifulSoup


def simple_get(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

    with closing(get(url, headers=headers, stream=True)) as resp:
        if is_good(resp):
            return resp.content
        else:
            return None


def is_good(resp):
    print resp
    content_type = resp.headers['Content-type'].lower()
    if resp.status_code == 200 and content_type.find('html') > -1:
        return True
    else:
        return False

def get_price(content):
    
    html = BeautifulSoup(content, 'html.parser')
    price = html.select('span#priceblock_ourprice')[0].text
    price = price[1:]
    price = price.replace(",","")

    return price
