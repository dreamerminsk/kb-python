import requests
from bs4 import BeautifulSoup

s = requests.Session()


def get_page(ref):
    try:
        r = s.get(ref, timeout=24)
        doc = BeautifulSoup(r.text, 'html.parser')
        return doc, None
    except Exception as ex:
        return None, ex
