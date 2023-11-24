import requests


class HhAPI:
    """
    Класс для подключения по API к HH.ru и получения нужных данных
    """

    def __init__(self):
        self.employers_monitoring_list = {'Бриз': 4647204,
                                          'WiseTech': 4187891,
                                          'delovoy.tech': 10017044,
                                          'sputnikfund.ru': 5560707,
                                          'postelka.ru': 1247819,
                                          'делу-время.рф': 2693346,
                                          'Scholastic Network': 3625115,
                                          'НОВАЯ ГОРНАЯ УК': 2688858,
                                          'ТОО Improvado KZ': 9574451,
                                          'kontinent.tomsk.ru': 1836747}

    def get_emps(self):

        """
        Метод для получения информации работодателей
        """

        emps_list = []

        for key, value in self.employers_monitoring_list.items():
            hh_request = requests.get(f'https://api.hh.ru/employers/{value}').json()

            emp_dict = {'employer_id': hh_request['id'],
                        'employer_name': hh_request['name'],
                        'description': hh_request['description'],
                        'employer_vacs_url': hh_request['vacancies_url'],
                        'employer_site_url': hh_request['site_url']}

            emps_list.append(emp_dict)

        return emps_list

    def get_vacs(self):

        """
        Метод для получения информации вакансий
        """

        vacs_list = []

        for key, value in self.employers_monitoring_list.items():

            hh_request = requests.get(f'https://api.hh.ru/vacancies?employer_id={value}').json()

            for i in range(len(hh_request['items'])):

                vac_dict = {'vac_employer_id': value,
                            'vac_id': hh_request['items'][i]['id'],
                            'vac_name': hh_request['items'][i]['name'],
                            'description': hh_request['items'][i]['snippet']['requirement'],
                            'vacs_url': hh_request['items'][i]['alternate_url']}
                try:
                    vac_dict['salary_from'] = hh_request['items'][i]['salary']['from']
                    vac_dict['salary_to'] = hh_request['items'][i]['salary']['to']

                except Exception:
                    vac_dict['salary_from'] = None
                    vac_dict['salary_to'] = None

                vacs_list.append(vac_dict)

        return vacs_list
