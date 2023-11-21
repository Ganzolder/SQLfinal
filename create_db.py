import psycopg2


def create_db():
    conn = psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password='12345'
    )

    conn.autocommit = True
    cursor = conn.cursor()

    create_db = f'CREATE DATABASE "HH.ru" ' \
                f'WITH ' \
                f'OWNER = postgres ' \
                f'ENCODING = "UTF8" ' \
                f'LC_CTYPE = "Russian_Russia.1251" ' \
                f'LC_COLLATE = "Russian_Russia.1251" ' \
                f'TABLESPACE = pg_default ' \
                f'CONNECTION LIMIT = -1 ' \
                f'IS_TEMPLATE = False;'

    cursor.execute(create_db)

    cursor.close()
    conn.close()


def create_tbls():
    conn = psycopg2.connect(
        host='localhost',
        database='HH.ru',
        user='postgres',
        password='12345'
    )

    conn.autocommit = True
    cursor = conn.cursor()
    create_db = f'CREATE TABLE employer_info (' \
                f'employer_id INT PRIMARY KEY, ' \
                f'employer_name VARCHAR(100) NOT NULL, ' \
                f'description TEXT, ' \
                f'employer_vacs_url VARCHAR, ' \
                f'employer_site_url VARCHAR)'

    cursor.execute(create_db)

    create_db = f'CREATE TABLE vacs_info (' \
                f'vac_employer_id INT, ' \
                f'vac_id INT PRIMARY KEY, ' \
                f'vac_name VARCHAR(100), ' \
                f'description TEXT, ' \
                f'vacs_url VARCHAR, ' \
                f'salary_from INT, ' \
                f'salary_to INT, ' \
                f'FOREIGN KEY (vac_employer_id) REFERENCES employer_info(employer_id))'

    cursor.execute(create_db)

    cursor.close()
    conn.close()


create_db()
create_tbls()