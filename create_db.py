import psycopg2


def create_db():

    """
    Функция создания базы данных
    """

    conn = psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password='12345'
    )

    conn.autocommit = True
    cursor = conn.cursor()

    create_dbase = 'CREATE DATABASE "HH.ru" ' \
                   'WITH ' \
                   'OWNER = postgres ' \
                   'ENCODING = "UTF8" ' \
                   'LC_CTYPE = "Russian_Russia.1251" ' \
                   'LC_COLLATE = "Russian_Russia.1251" ' \
                   'TABLESPACE = pg_default ' \
                   'CONNECTION LIMIT = -1 ' \
                   'IS_TEMPLATE = False;'

    cursor.execute(create_dbase)

    cursor.close()
    conn.close()


def create_tbls():
    """
    Функция создания базы таблиц базы данных
    """

    conn = psycopg2.connect(
        host='localhost',
        database='HH.ru',
        user='postgres',
        password='12345'
    )

    conn.autocommit = True
    cursor = conn.cursor()
    create_tb = 'CREATE TABLE employer_info (' \
                'employer_id INT PRIMARY KEY, ' \
                'employer_name VARCHAR(100) NOT NULL, ' \
                'description TEXT, ' \
                'employer_vacs_url VARCHAR, ' \
                'employer_site_url VARCHAR)'

    cursor.execute(create_tb)

    create_tb = 'CREATE TABLE vacs_info (' \
                'vac_employer_id INT, ' \
                'vac_id INT PRIMARY KEY, ' \
                'vac_name VARCHAR(100), ' \
                'description TEXT, ' \
                'vacs_url VARCHAR, ' \
                'salary_from INT, ' \
                'salary_to INT, ' \
                'FOREIGN KEY (vac_employer_id) REFERENCES employer_info(employer_id))'

    cursor.execute(create_tb)

    cursor.close()
    conn.close()


create_db()
create_tbls()
