from dateutil.parser import parse

from kb import urls
from net import get_page
from store import save_weekend
from utils import num

doc, err = get_page(urls['weekends'])
rows = doc.select('table.calendar_year tbody tr')


def parse_weekend(week):
    pass


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
