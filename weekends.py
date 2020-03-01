import time

from dateutil.parser import parse

from kb import urls, getweekend
from net import get_page
from store import save_weekend, save_film, save_weekend_boxoffice
from utils import num


def parse_weekend(week):
    print(getweekend(week['weekend']))
    time.sleep(4)
    d, e = get_page(getweekend(week['weekend']))
    rs = d.select('table#krestable tr')
    for r in rs[1:]:
        cs = r.select('td')
        film = {}
        boxoffice = {'weekend': str(week['weekend'].date())}
        for idx, c in enumerate(cs):
            print(idx, c)
            if idx == 1:
                boxoffice['pos'] = c.text
                print('\tpos: ', boxoffice['pos'])
            if idx == 3:
                print('\ttitle: ', c.text)
                film['title'] = c.text
                print('\tpage: ', c.select_one('a')['href'])
                film['page'] = c.select_one('a')['href']
                print('\tname: ', c.select_one('a')['rel'])
                film['id'] = c.select_one('a')['rel'][0]
                boxoffice['film'] = c.select_one('a')['rel'][0]
            if idx == 4:
                print('\toriginal: ' + c.text)
                film['original'] = c.text
            if idx == 5:
                print('\tdistributor: ' + c.text)
                boxoffice['distributor'] = c.text
            if idx == 6:
                print('\tweekendRur: ' + c.text)
                boxoffice['weekend_rur'] = num(c.text)
            if idx == 8:
                print('\tscreens: ' + c.text)
                boxoffice['screens'] = num(c.text)
            if idx == 10:
                print('\tdays: ' + c.text)
                boxoffice['days'] = num(c.text)
            if idx == 11:
                print('\ttotalRur: ' + c.text)
                boxoffice['total_rur'] = num(c.text)
            if idx == 12:
                print('\tspectaculars: ' + c.text)
                boxoffice['spectaculars'] = num(c.text)
        save_film(film)
        save_weekend_boxoffice(boxoffice)


doc, err = get_page(urls['weekends'])
rows = doc.select('table.calendar_year tbody tr')
for row in rows:
    cells = row.select('td')
    weekend = {}
    for index, cell in enumerate(cells):
        print(index, cell)
        if index == 0:
            print('\ttitle: ', cell.text)
            weekend['title'] = cell.text
            print('\tpage: ', cell.select_one('a')['href'])
            weekend['page'] = cell.select_one('a')['href']
            parts = cell.select_one('a')['href'].split('/')
            weekend['weekend'] = parse(parts[-2], dayfirst=True)
        if index == 1:
            print('\ttotalRur: ' + cell.text)
            weekend['total_rur'] = num(cell.text)
        if index == 3:
            print('\tfilms: ' + cell.text)
            weekend['films'] = num(cell.text)
    save_weekend(weekend)
    parse_weekend(weekend)
