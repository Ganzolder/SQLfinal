from HHAPI import HhAPI
from db_uploader import DbUploader
from DBManager import DBManager


# обновление базы данных
get_HhApi = HhAPI()

emp_list = get_HhApi.get_emps()
vac_list = get_HhApi.get_vacs()

db_uploader = DbUploader()

db_uploader.upload_data('employer_info', emp_list)
db_uploader.upload_data('vacs_info', vac_list)

if __name__ == '__main__':
    print(f'Добро пожловать в менеджер сборщик вакансий вакансий!'
          f'Я уже обновил вакансии в базе по следующим компаниям:\n'
          f'Бриз, WiseTech, delovoy.tech, sputnikfund.ru, postelka.ru, делу-время.рф, Scholastic Network, '
          f'НОВАЯ ГОРНАЯ УК, ТОО Improvado KZ, kontinent.tomsk.ru')

    dbmanager = DBManager()

    vacs_count = len(dbmanager.get_all_vacancies())

    print(f'На данный момент в базе {vacs_count} вакансий\n')

    user_choice = int(input(f'Выбери один из пунктов, чтобы получить информацию:\n'
          f'1. Получить список всех компаний и количество вакансий у каждой компании.\n'
          f'2. Получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.\n'
          f'3. Получить среднюю зарплату по вакансиям.\n'
          f'4. Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям.\n'
          f'5. Получить список всех вакансий, в названии которых содержатся переданные в метод слова, например python.\n'
          f'\n0. В любой момент, чтобы завершить работу.\n'))


    match user_choice:
        case 1:

            results = dbmanager.get_companies_and_vacancies_count()

            for row in results:
                print(f'Компания "{row[1]}" открытых вакансий - {row[2]}')

        case 2:

            results = dbmanager.get_all_vacancies()

            for row in results:
                print(f'Вакансия "{row[0]}", компания "{row[1]}", зарплата от {row[2]} до {row[3]}, ссылка {row[4]}')

        case 3:

            results = dbmanager.get_avg_salary()

            for row in results:
                print(f'Средняя ЗП по собранным вакансиям {int((row[0] + row[1])/2)}р.')

        case 4:

            results = dbmanager.get_vacancies_with_higher_salary()

            for row in results:
                print(f'Вакансия "{row[2]}", зарплата от {row[5]}, ссылка {row[4]}')

        case 5:

            key_word = input(f'\nВведите ключевое слово для поиска:\n')
            results = dbmanager.get_vacancies_with_keyword(key_word)

            for row in results:
                print(f'Вакансия "{row[2]}", зарплата от {row[5]}, ссылка {row[4]}')

        case _:
            exit()
