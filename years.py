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


page, err = get_page('http://kinobusiness.com/kassovye_sbory/films_year/')
doc = BeautifulSoup(page.text, 'html.parser')
