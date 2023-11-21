import psycopg2
import re


class DbUploader:

    """
    Класс для загрузки данных в БД
    """

    def __init__(self):
        pass

    @staticmethod
    def upload_data(table_name, upload_name_list):
        conn = psycopg2.connect(
            host='localhost',
            database='HH.ru',
            user='postgres',
            password='12345'
        )

        conn.autocommit = True
        cursor = conn.cursor()

        sql_comm = f'TRUNCATE TABLE {table_name} CASCADE'
        cursor.execute(sql_comm)

        columns_count = len(upload_name_list[0]) - 1
        sql_comm = f'INSERT INTO {table_name} VALUES ({"%s, " * columns_count}%s)'

        for i in range(len(upload_name_list)):
            db_values = []
            for key, value in upload_name_list[i].items():
                try:
                    int(value)
                    db_values.append(value)
                except Exception:
                    try:
                        cleaned_string = re.sub(r'<[^>]+>', '', value)
                        db_values.append(cleaned_string)
                    except Exception:
                        db_values.append(None)

            cursor.execute(sql_comm, db_values)


