from kb import urls
from net import get_page
from store import conn

doc, err = get_page(urls['weekends'])
rows = doc.select('table.calendar_tbody year tr')
for row in rows:
    cells = row.select('td')
    film = {}
    for index, cell in enumerate(cells):
        print(index, cell)
        if index == 0:
            print('\tpos: ', cell.text)
        if index == 1:
            print('\ttitle: ', cell.text)
            film['title'] = cell.text
            print('\tpage: ', cell.select_one('a')['href'])
            film['page'] = cell.select_one('a')['href']
            print('\tname: ', cell.select_one('a')['name'])
            film['id'] = cell.select_one('a')['name']
        if index == 2:
            print('\toriginal: ' + cell.text)
            film['original'] = cell.text
        if index == 3:
            print('\tdistributor: ' + cell.text)
        if index == 4:
            print('\tscreens: ' + cell.text)
        if index == 5:
            print('\ttotalRur: ' + cell.text)
        if index == 6:
            print('\ttotalUsd: ' + cell.text)
        if index == 7:
            print('\tspectaculars: ' + cell.text)
        if index == 8:
            print('\tdays: ' + cell.text)
    try:
        r = conn.execute('INSERT INTO `kb-films`(id,title,original,page) VALUES(?,?,?,?)',
                         [film['id'], film['title'], film['original'], film['page']])
        conn.commit()
        print(r)
    except Exception as e:
        print(e)
