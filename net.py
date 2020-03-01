import requests
from bs4 import BeautifulSoup

s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'})


def get_page(ref):
    try:
        r = s.get(ref, timeout=24)
        html = BeautifulSoup(r.text, 'html.parser')
        return html, None
    except Exception as ex:
        print(ex)
        return None, ex
