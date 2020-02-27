from dateutil.parser import parse

from kb import urls
from net import get_page

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
            weekend['weekend'] = parse(parts[-2])
        if index == 1:
            print('\ttotalRur: ' + cell.text)
            weekend['total_rur'] = cell.text
        if index == 3:
            print('\tfilms: ' + cell.text)
