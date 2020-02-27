import sqlite3

conn = sqlite3.connect("kb.db")

conn.execute('CREATE TABLE IF NOT EXISTS `kb-films` (`id` INTEGER PRIMARY KEY, `title` TEXT, original TEXT, '
             '`page` TEXT)')
