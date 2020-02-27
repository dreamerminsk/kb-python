from kb import urls
from net import get_page

doc, err = get_page(urls['weekends'])
rows = doc.select('table.calendar_tbody year tr')
for row in rows:
    cells = row.select('td')
    film = {}
    for index, cell in enumerate(cells):
        print(index, cell)
        if index == 0:
            print('\ttitle: ', cell.text)
            # film['title'] = cell.text
            print('\tpage: ', cell.select_one('a')['href'])
            # film['page'] = cell.select_one('a')['href']
        if index == 1:
            print('\ttotalRur: ' + cell.text)
        if index == 3:
            print('\tfilms: ' + cell.text)
