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


doc, err = get_page('http://kinobusiness.com/kassovye_sbory/films_year/')
print(doc)
rows = doc.select('table.calendar_year tr')
for row in rows[1:]:
    print(row)
    cells = row.select('td')
