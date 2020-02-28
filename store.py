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


def save_boxoffice(boxoffice):
    try:
        conn.execute(
            'INSERT INTO `kb-years`(film,distributor,pos,total_rur, total_usd,screens,spectaculars,days) '
            'VALUES(?,?,?,?,?,?,?,?)',
            [boxoffice['film'], boxoffice['distributor'], boxoffice['pos'], boxoffice['total_rur'],
             boxoffice['total_usd'], boxoffice['screens'], boxoffice['spectaculars'],
             boxoffice['days']])
        conn.commit()
    except Exception as e:
        print(e)
        try:
            conn.execute(
                'UPDATE `kb-years` SET pos=?,total_rur=?, total_usd=?,screens=?,spectaculars=?,days=? WHERE film=?',
                [boxoffice['pos'], boxoffice['total_rur'], boxoffice['total_usd'], boxoffice['screens'],
                 boxoffice['spectaculars'], boxoffice['days'], boxoffice['film']])
            conn.commit()
        except Exception as e:
            print(e)


def save_weekend(weekend):
    try:
        conn.execute('INSERT INTO `kb-weekends`(weekend,title,page, total_rur, films) VALUES(?,?,?,?,?)',
                     [weekend['weekend'], weekend['title'], weekend['page'], weekend['total_rur'], weekend['films']])
        conn.commit()
    except Exception as e:
        print(e)
        try:
            conn.execute(
                'UPDATE `kb-weekends` SET total_rur=?,films=? WHERE weekend=?',
                [weekend['total_rur'], weekend['films'], weekend['weekend']])
            conn.commit()
        except Exception as e:
            print(e)


def save_thursday(thursday):
    try:
        conn.execute('INSERT INTO `kb-thursdays`(thursday,title,page, total_rur) VALUES(?,?,?,?)',
                     [thursday['thursday'], thursday['title'], thursday['page'], thursday['total_rur']])
        conn.commit()
    except Exception as e:
        print(e)
        try:
            conn.execute(
                'UPDATE `kb-thursdays` SET total_rur=? WHERE thursday=?',
                [thursday['total_rur'], thursday['thursday']])
            conn.commit()
        except Exception as e:
            print(e)
