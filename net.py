import requests
from bs4 import BeautifulSoup

s = requests.Session()


def get_page(ref):
    try:
        r = s.get(ref, timeout=24)
        html = BeautifulSoup(r.text, 'html.parser')
        return html, None
    except Exception as ex:
        print(ex)
        return None, ex
