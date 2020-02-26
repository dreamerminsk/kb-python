import requests
from bs4 import BeautifulSoup

def get_page(ref):
    try:
        r = s.get(ref, timeout=24)
        doc = BeautifulSoup(r.text, 'html.parser')
        return doc, None
    except Exception as ex:
        return None, ex

s = requests.Session()
doc, err = get_page('http://kinobusiness.com/kassovye_sbory/films_year/')
rows = doc.select('table.calendar_year tr')
for row in rows[1:]:
    cell: object = row.select('td')
    print(cell)
    row.select('td')
