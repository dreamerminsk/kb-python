from dateutil.parser import parse

from kb import urls, getweekend
from net import get_page
from store import save_weekend
from utils import num

doc, err = get_page(urls['weekends'])
rows = doc.select('table.calendar_year tbody tr')


def parse_weekend(week):
    doc, err = get_page(getweekend(week['weekend']))
    rows = doc.select('table.calendar_year tr')

    for row in rows[1:]:
        cells = row.select('td')
        film = {}
        boxoffice = {}
        for index, cell in enumerate(cells):
            print(index, cell)
            if index == 1:
                print('\tpos: ', cell.text)
                boxoffice['pos'] = cell.text
            if index == 3:
                print('\ttitle: ', cell.text)
                film['title'] = cell.text
                print('\tpage: ', cell.select_one('a')['href'])
                film['page'] = cell.select_one('a')['href']
                print('\tname: ', cell.select_one('a')['name'])
                film['id'] = cell.select_one('a')['name']
                boxoffice['film'] = cell.select_one('a')['name']
            if index == 4:
                print('\toriginal: ' + cell.text)
                film['original'] = cell.text
            if index == 5:
                print('\tdistributor: ' + cell.text)
                boxoffice['distributor'] = cell.text
            if index == 4:
                print('\tscreens: ' + cell.text)
                boxoffice['screens'] = num(cell.text)
            if index == 5:
                print('\ttotalRur: ' + cell.text)
                boxoffice['total_rur'] = num(cell.text)
            if index == 6:
                print('\ttotalUsd: ' + cell.text)
                boxoffice['total_usd'] = num(cell.text)
            if index == 7:
                print('\tspectaculars: ' + cell.text)
                boxoffice['spectaculars'] = num(cell.text)
            if index == 8:
                print('\tdays: ' + cell.text)
                boxoffice['days'] = num(cell.text)
        # save_film(film)
        # save_boxoffice(boxoffice)


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
