from config import connect_db

from support import read_json_file
from part_database.db_for_catalog import show_list_catalog, get_id_by_name

connect, cursor = connect_db('project_litres', '123', 'postgres', 'localhost')

# data_book = read_json_file('../part_parser/books.json')


def create_db_books():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS data_books(
        book_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        title TEXT,
        img_link TEXT,
        author TEXT,
        price TEXT,
        estimation TEXT,
        estimation_quantity TEXT,
        type_book TEXT,
        link_detail TEXT,
        catalog_id INTEGER REFERENCES catalog(catalog_id)
    );
    ''')
    connect.commit()
    print('База данных создалась')


# create_db_books()


def add_data_books(obj):
    title_catalog = show_list_catalog()
    for title in title_catalog:
        for item in obj:
            if title in item:
                cat_id = get_id_by_name(title)
                cursor.execute('''
                    INSERT INTO data_books(title, img_link, author, price,
                                     estimation, estimation_quantity, type_book, 
                                     link_detail, catalog_id)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ''', (item[title]['title'], item[title]['img_link'], item[title]['author'], item[title]['price'],
                      item[title]['estimation'], item[title]['estimation_quantity'], item[title]['type_book'],
                      item[title]['link_detail'], cat_id))
                connect.commit()
                print(f'Данный категории --- {cat_id} добавлены')


# add_data_books(data_book)


def show_list_book_by_cat_id(catalog_id):
    cursor.execute("""
        SELECT title FROM data_books WHERE catalog_id = %s
    """, (catalog_id, ))
    list_book = cursor.fetchall()
    return [i[0] for i in list_book]


def show_book_info(name_book):
    cursor.execute("""
        SELECT title, img_link, author, price, estimation, estimation_quantity, type_book FROM data_books WHERE title = %s
    """, (name_book, ))
    list_book = cursor.fetchone()
    return list_book


def show_link_detail_by_name_book(title):
    cursor.execute("""
        SELECT link_detail FROM data_books WHERE title = %s
    """, (title, ))
    return cursor.fetchone()[0]


