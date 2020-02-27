from kb import urls
from net import get_page
from store import save_film, save_boxoffice
from utils import num

doc, err = get_page(urls['year'])
rows = doc.select('table.calendar_year tr')

for row in rows[1:]:
    cells = row.select('td')
    film = {}
    boxoffice = {}
    for index, cell in enumerate(cells):
        print(index, cell)
        if index == 0:
            print('\tpos: ', cell.text)
            boxoffice['pos'] = cell.text
        if index == 1:
            print('\ttitle: ', cell.text)
            film['title'] = cell.text
            print('\tpage: ', cell.select_one('a')['href'])
            film['page'] = cell.select_one('a')['href']
            print('\tname: ', cell.select_one('a')['name'])
            film['id'] = cell.select_one('a')['name']
            boxoffice['film'] = cell.select_one('a')['name']
        if index == 2:
            print('\toriginal: ' + cell.text)
            film['original'] = cell.text
        if index == 3:
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
    save_film(film)
    save_boxoffice(boxoffice)
