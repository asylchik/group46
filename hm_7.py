import sqlite3
conn = sqlite3.connect('hm.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title TEXT NOT NULL CHECK(LENGTH(product_title) <= 200),
    price REAL NOT NULL DEFAULT 0.0 CHECK(price >= 0),
    quantity INTEGER NOT NULL DEFAULT 0 CHECK(quantity >= 0)
)
''')
conn.commit()


def add_product():
    products = [
        ('Мыло детское', 50.5, 20),
        ('Шампунь для волос', 150.0, 10),
        ('Гель для душа', 80.75, 15),
        ('Зубная паста', 60.0, 25),
        ('Мыло хозяйственное', 35.0, 30),
        ('Крем для рук', 120.0, 12),
        ('Шампунь для детей', 170.0, 8),
        ('Мыло жидкое с запахом ванили', 75.5, 18),
        ('Скраб для тела', 180.0, 6),
        ('Кондиционер для волос', 200.0, 7),
        ('Гель для умывания', 90.0, 13),
        ('Зубная щетка', 45.0, 22),
        ('Лосьон для тела', 140.0, 9),
        ('Крем для лица', 210.0, 5),
        ('Губка для посуды', 20.0, 50),
    ]
    cursor.executemany('INSERT INTO products(product_title, price, quantity) VALUES(?, ?, ?)', products)
    conn.commit()


def update_quantity(product_id, new_quantity):
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))
    conn.commit()


def update_price(product_id, new_price):
    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
    conn.commit()


def delete_product(product_id):
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()


def fetch_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for product in products:
        print(product)


def fetch_products_price_quantity(price_limit, quantity_limit):
    cursor.execute('SELECT * FROM products WHERE price < ? AND quantity > ?', (price_limit, quantity_limit))
    products = cursor.fetchall()
    for product in products:
        print(product)


def search_product(keyword):
    cursor.execute('SELECT * FROM products WHERE product_title LIKE ?', (keyword,))
    products = cursor.fetchall()
    for product in products:
        print(product)


add_product()
fetch_products()
update_quantity(1, 25)
update_price(5, 145.99)
delete_product(3)
fetch_products_price_quantity(100, 5)
search_product('мыло')
conn.close()