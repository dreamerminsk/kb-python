import sqlite3

import requests
from bs4 import BeautifulSoup

conn = sqlite3.connect("kb.db")
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS `kb-films` (`id` INTEGER PRIMARY KEY, `title` TEXT, original TEXT, '
               '`page` TEXT)')


def num(text):
    return text.replace(' ', '').replace('*', '')


def get_page(ref):
    try:
        res = s.get(ref, timeout=24)
        html = BeautifulSoup(res.text, 'html.parser')
        return html, None
    except Exception as ex:
        return None, ex


s = requests.Session()
doc, err = get_page('http://kinobusiness.com/kassovye_sbory/films_year/')
rows = doc.select('table.calendar_year tr')


def save_film(f):
    try:
        cursor.execute('INSERT INTO `kb-films`(id,title,original,page) VALUES(?,?,?,?)',
                       [f['id'], f['title'], f['original'], f['page']])
        conn.commit()
    except Exception as e:
        print(e)


def save_boxoffioce(b):
    try:
        cursor.execute(
            'INSERT INTO `kb-years`(film,distributor,pos,total_rur, total_usd,screens,spectaculars,days) '
            'VALUES(?,?,?,?,?,?,?,?)',
            [b['film'], b['distributor'], b['pos'], b['total_rur'], b['total_usd'], b['screens'], b['spectaculars'],
             b['days']])
        conn.commit()
    except Exception as e:
        print(e)
        try:
            cursor.execute(
                'UPDATE `kb-years` SET pos=?,total_rur=?, total_usd=?,screens=?,spectaculars=?,days=? WHERE film=?',
                [b['pos'], b['total_rur'], b['total_usd'], b['screens'], b['spectaculars'], b['days'], b['film']])
            conn.commit()
        except Exception as e:
            print(e)


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
    save_boxoffioce(boxoffice)
