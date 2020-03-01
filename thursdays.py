import time

from dateutil.parser import parse

from kb import urls, get_thursday
from net import get_page
from store import save_thursday, save_film, save_thursday_boxoffice
from utils import num

doc, err = get_page(urls['thursdays'])
rows = doc.select('table.calendar_year tbody tr')


def parse_thursday(thday):
    print(get_thursday(thday['thursday']))
    time.sleep(4)
    d, e = get_page(get_thursday(thday['thursday']))
    ts = d.select('section.events__table table')
    rs = ts[0].select('tr')
    for r in rs[1:]:
        cs = r.select('td')
        film = {}
        boxoffice = {'thursday': str(thday['thursday'].date())}
        for idx, c in enumerate(cs):
            print(idx, c)
            if idx == 0:
                boxoffice['pos'] = c.text
                print('\tpos: ', boxoffice['pos'])
            if idx == 1:
                print('\ttitle: ', c.text)
                film['title'] = c.text
                print('\tpage: ', c.select_one('a')['href'])
                film['page'] = c.select_one('a')['href']
                print('\tname: ', c.select_one('a')['rel'])
                film['id'] = c.select_one('a')['rel'][0]
                boxoffice['film'] = c.select_one('a')['rel'][0]
            if idx == 2:
                print('\tdistributor: ' + c.text)
                boxoffice['distributor'] = c.text
            if idx == 3:
                print('\tthursdayRur: ' + c.text)
                boxoffice['thursday_rur'] = num(c.text)
        save_film(film)
        save_thursday_boxoffice(boxoffice)


for row in rows:
    cells = row.select('td')
    thursday = {}
    for index, cell in enumerate(cells):
        print(index, cell)
        if index == 0:
            print('\ttitle: ', cell.text)
            thursday['title'] = cell.text
            print('\tpage: ', cell.select_one('a')['href'])
            thursday['page'] = cell.select_one('a')['href']
            parts = cell.select_one('a')['href'].split('/')
            thursday['thursday'] = parse(parts[-2], dayfirst=True)
        if index == 1:
            print('\ttotalRur: ' + cell.text)
            thursday['total_rur'] = num(cell.text)
    save_thursday(thursday)
    parse_thursday(thursday)
