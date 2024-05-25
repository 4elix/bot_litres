from config import connect_db

connect, cursor = connect_db('project_litres', '123', 'postgres', 'localhost')


def create_db_user():
    cursor.execute("""
        DROP TABLE IF EXISTS users;
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            user_name TEXT,
            language TEXT,
            tg_id BIGINT NOT NULL UNIQUE 
        );
    """)
    connect.commit()


# create_db_user()


def add_user(user_name, language, tg_id):
    cursor.execute("""
        INSERT INTO users(user_name, language, tg_id)
        VALUES (%s, %s, %s);
    """, (user_name, language, tg_id))
    connect.commit()


def search_user_by_tg_id(tg_id):
    cursor.execute("""
        SELECT * FROM users WHERE tg_id = %s
    """, (tg_id,))
    return cursor.fetchone()


def get_lang_by_tg_id(tg_id):
    cursor.execute("""
        SELECT language FROM users WHERE tg_id = %s
    """, (tg_id,))
    return cursor.fetchone()[0]


def delete_account(tg_id):
    cursor.execute("""
        DELETE FROM users WHERE tg_id = %s
    """, (tg_id,))
    connect.commit()


def update_lang(lang, tg_id):
    cursor.execute("""
        UPDATE users
        SET language = %s WHERE tg_id = %s
    """, (lang, tg_id))
    connect.commit()
