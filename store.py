import sqlite3

conn = sqlite3.connect("kb.db")

conn.execute('CREATE TABLE IF NOT EXISTS `kb-films` (`id` INTEGER PRIMARY KEY, `title` TEXT, original TEXT, '
             '`page` TEXT)')


def save_film(f):
    try:
        conn.execute('INSERT INTO `kb-films`(id,title,original,page) VALUES(?,?,?,?)',
                     [f['id'], f['title'], f['original'], f['page']])
        conn.commit()
    except Exception as e:
        print(e)


def save_boxoffice(b):
    try:
        conn.execute(
            'INSERT INTO `kb-years`(film,distributor,pos,total_rur, total_usd,screens,spectaculars,days) '
            'VALUES(?,?,?,?,?,?,?,?)',
            [b['film'], b['distributor'], b['pos'], b['total_rur'], b['total_usd'], b['screens'], b['spectaculars'],
             b['days']])
        conn.commit()
    except Exception as e:
        print(e)
        try:
            conn.execute(
                'UPDATE `kb-years` SET pos=?,total_rur=?, total_usd=?,screens=?,spectaculars=?,days=? WHERE film=?',
                [b['pos'], b['total_rur'], b['total_usd'], b['screens'], b['spectaculars'], b['days'], b['film']])
            conn.commit()
        except Exception as e:
            print(e)


def save_weekend(w):
    try:
        conn.execute('INSERT INTO `kb-weekends`(weekend,title,page, total_rur, films) VALUES(?,?,?,?,?)',
                     [w['weekend'], w['title'], w['page'], w['total_rur'], w['films']])
        conn.commit()
    except Exception as e:
        print(e)
        try:
            conn.execute(
                'UPDATE `kb-weekends` SET total_rur=?,films=? WHERE weekend=?',
                [w['total_rur'], w['films'], w['weekend']])
            conn.commit()
        except Exception as e:
            print(e)
