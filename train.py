import sqlite3

db = sqlite3.connect("Books.db")

c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS book (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    year INTEGER,
    available INTEGER)""")

c.executemany(
    "INSERT OR IGNORE INTO book (id, title, author, year, available) VALUES (?, ?, ?, ?, ?)",
    [
        (1, 'Война и мир', 'Лев Толстой', 1869, 1),
        (2, 'Преступление и наказание', 'Фёдор Достоевский', 1866, 1),
        (3, 'Мастер и Маргарита', 'Михаил Булгаков', 1967, 0),
        (4, '1984', 'Джордж Оруэлл', 1949, 1),
        (5, 'Гарри Поттер и философский камень', 'Дж. К. Роулинг', 1997, 1)
    ]
)
c.execute("UPDATE book SET available = 0 WHERE id = 5")
c.execute("SELECT * FROM book WHERE author = 'Лев Толстой'")
c.execute("DELETE FROM book WHERE year < 2000")
db.commit()


db.close()