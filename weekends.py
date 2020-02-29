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
    rows = d.select('table#krestable > tbody > tr')
    for row in rows[1:]:
        cells = row.select('td')
        film = {}
        boxoffice = {}
        boxoffice['weekend'] = week['weekend']
        for index, cell in enumerate(cells):
            print(index, cell)
            if index == 1:
                boxoffice['pos'] = cell.text
                print('\tpos: ', boxoffice['pos'])
            if index == 3:
                print('\ttitle: ', cell.text)
                film['title'] = cell.text
                print('\tpage: ', cell.select_one('a')['href'])
                film['page'] = cell.select_one('a')['href']
                print('\tname: ', cell.select_one('a')['rel'])
                film['id'] = cell.select_one('a')['rel']
                boxoffice['film'] = cell.select_one('a')['rel']
            if index == 4:
                print('\toriginal: ' + cell.text)
                film['original'] = cell.text
            if index == 5:
                print('\tdistributor: ' + cell.text)
                boxoffice['distributor'] = cell.text
            if index == 6:
                print('\tweekendRur: ' + cell.text)
                boxoffice['weekend_rur'] = num(cell.text)
            if index == 8:
                print('\tscreens: ' + cell.text)
                boxoffice['screens'] = num(cell.text)
            if index == 10:
                print('\tdays: ' + cell.text)
                boxoffice['days'] = num(cell.text)
            if index == 11:
                print('\ttotalRur: ' + cell.text)
                boxoffice['total_rur'] = num(cell.text)
            if index == 12:
                print('\tspectaculars: ' + cell.text)
                boxoffice['spectaculars'] = num(cell.text)
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
