from dateutil.parser import parse

from kb import urls
from net import get_page
from store import save_thursday
from utils import num

doc, err = get_page(urls['thursdays'])
rows = doc.select('table.calendar_year tbody tr')

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
    print(thursday['thursday'])
