import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('''
    CREATE TABLE vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        valor REAL NOT NULL,
        data_hora TEXT NOT NULL
    )
''')
conn.close()
