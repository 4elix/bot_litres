from config import connect_db

from support import read_json_file


connect, cursor = connect_db('project_litres', '123', 'postgres', 'localhost')

# catalog_data = read_json_file('../part_parser/catalog.json')


def create_db_catalog():
    cursor.execute("""
        DROP TABLE IF EXISTS catalog;
        CREATE TABLE IF NOT EXISTS catalog(
            catalog_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            catalog_name TEXT
        );
    """)
    connect.commit()


# create_db_catalog()


def add_data_catalog(obj):
    for item in obj:
        cursor.execute("""
            INSERT INTO catalog(catalog_name)
            VALUES(%s);
        """, (item['title'], ))
        connect.commit()


# add_data_catalog(catalog_data)


def show_list_catalog():
    cursor.execute("""
        SELECT catalog_name FROM catalog;
    """)
    data_catalog = cursor.fetchall()
    return [item[0] for item in data_catalog]


def get_id_by_name(name):
    cursor.execute('''
        SELECT catalog_id FROM catalog WHERE catalog_name = %s
    ''', (name, ))
    cat_id = cursor.fetchone()
    return cat_id[0]


