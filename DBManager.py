import psycopg2


class DBManager:

    """
    Класс для работы с базой данных и извлечения данных из БД
    """

    def __init__(self):
        pass

    @staticmethod
    def db_request(request):

        """
        Метод для подключения, отправки и получения запросов из БД
        """

        conn = psycopg2.connect(
            host='localhost',
            database='HH.ru',
            user='postgres',
            password='12345'
        )

        conn.autocommit = True
        cursor = conn.cursor()

        cursor.execute(request)

        results = cursor.fetchall()

        # Закрываем соединение
        cursor.close()
        conn.close()

        return results

    def get_companies_and_vacancies_count(self):

        sql_comm = f'SELECT employer_id, employer_name, COUNT(vacs_info.vac_id) AS num_vacs' \
                   f' FROM employer_info' \
                   f' LEFT JOIN vacs_info' \
                   f' ON employer_info.employer_id = vacs_info.vac_employer_id' \
                   f' GROUP BY employer_id, employer_name' \
                   f' ORDER BY num_vacs'

        results = self.db_request(sql_comm)

        return results

    def get_all_vacancies(self):

        sql_comm = f'SELECT vac_name, employer_name, salary_from, salary_to, vacs_url ' \
                   f'FROM employer_info ' \
                   f'LEFT JOIN vacs_info ON employer_info.employer_id = vacs_info.vac_employer_id'

        results = self.db_request(sql_comm)

        return results

    def get_avg_salary(self):

        sql_comm = f'SELECT AVG(salary_from), AVG(salary_to) FROM vacs_info'

        results = self.db_request(sql_comm)

        return results

    def get_vacancies_with_higher_salary(self):

        sql_comm = f'SELECT * FROM vacs_info ' \
                   f'WHERE salary_from > (' \
                   f'SELECT AVG(salary_from + salary_to) ' \
                   f'FROM vacs_info)'

        results = self.db_request(sql_comm)

        return results

    def get_vacancies_with_keyword(self, key_word):

        sql_comm = f"SELECT * FROM vacs_info WHERE vac_name ILIKE '%{key_word}%';"

        results = self.db_request(sql_comm)

        return results



