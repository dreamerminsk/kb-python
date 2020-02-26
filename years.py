import sqlite3

import requests
from bs4 import BeautifulSoup

conn = sqlite3.connect("kb.db")
cursor = conn.cursor()


def get_page(ref):
    try:
        r = s.get(ref, timeout=24)
        html = BeautifulSoup(r.text, 'html.parser')
        return html, None
    except Exception as ex:
        return None, ex


s = requests.Session()
doc, err = get_page('http://kinobusiness.com/kassovye_sbory/films_year/')
rows = doc.select('table.calendar_year tr')
for row in rows[1:]:
    cells = row.select('td')
    for index, cell in enumerate(cells):
        print(index, cell)
        if index == 0:
            print('\tpos: ', cell.text)
        if index == 1:
            print('\ttitle: ', cell.text)
            print('\tpage: ', cell.select_one('a')['href'])
            print('\tname: ', cell.select_one('a')['name'])
