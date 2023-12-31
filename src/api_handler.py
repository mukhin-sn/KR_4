import requests
import os
from src.file_handler import *


class APIHandler(ABC):
    """
    Абстрактный класс для работы с API сайтов
    """

    @abstractmethod
    def api_handler(self, vacancy_name: str, vacancy_city: str):
        """
        Абстрактный метод для работы с API сайтов
        """
        pass


class SuperJobAPI(APIHandler):
    """
    Класс для работы с API сайта superjob.ru
    """

    def __init__(self):
        self.host = 'https://api.superjob.ru/2.0/vacancies/'
        self.__api_key = os.getenv('SJ_API_KEY')
        self.head = {"X-Api-App-Id": self.__api_key}
        self.resp = requests.get(self.host, headers=self.head).request.headers

    def __str__(self):
        return ", ".join([f"{key}: {self.resp[key]}" for key in self.resp])

    def api_handler(self, vacancy_name: str, vacancy_city=None) -> list:
        """
        Метод получения списка вакансий, согласно фильтру
        :param vacancy_name: - строка для фильтра вакансий
        :param vacancy_city: - город, для поиска вакансий
        :return: -> отформатированный по требуемым полям список вакансий
        """

        # список, полученных при запросе к сайту, вакансий
        list_vacancy = []

        # список, который будет возвращать функция
        out_list_vacancy = []

        # параметры, передаваемые в GET запросе
        params = {
            "count": 100,
            "archive": False,
            "keyword": vacancy_name,
            "period": 0,
            "town": vacancy_city
            }

        # просмотр максимального количества вакансий, которое может вернуть сервер по запросу (500 шт.)
        for num_page in range(5):
            params["page"] = num_page
            list_vacancy.extend(requests.get(self.host, headers=self.head, params=params).json()["objects"])

        for vac in list_vacancy:
            # определяем максимальную величину заработной платы, предлагаемой по вакансии
            # :param sal: максимальна величина заработной платы, предлагаемой по вакансии
            sal = str(max(vac['payment_from'], vac['payment_to']))

            # форматируем вакансию для передачи в выходной список
            vac_dict = dict(id=str(vac['id']),
                            name=vac['profession'],
                            city=vac['town']['title'],
                            description=vac['candidat'],
                            salary=sal,
                            currency=vac['currency'],
                            url=vac['link'])

            # формируем выходной список
            out_list_vacancy.append(vac_dict)

        return out_list_vacancy


class HHruAPI(APIHandler):
    """Класс для работы с API сайта hh.ru"""

    def __init__(self):
        self.host = 'https://api.hh.ru/vacancies/'
        self.resp = requests.get(self.host).request.headers

    def __str__(self):
        return ", ".join([f"{key}: {self.resp[key]}" for key in self.resp])

    def api_handler(self, vacancy_name: str, vacancy_city=None) -> list:
        """
        Метод получения списка вакансий в Российском сегменте, согласно фильтру
        :param vacancy_name: - строка для фильтра вакансий
        :param vacancy_city: - город, для поиска вакансий
        :return: -> отформатированный по требуемым полям список вакансий
        """
        # список, полученных при запросе к сайту, вакансий
        list_vacancy = []

        # список, который будет возвращать функция
        out_list_vacancy = []

        # параметры, передаваемые в GET запросе
        params = {
            "per_page": 100,
            "area": 113,
            "text": f"NAME:{vacancy_name}",
        }

        # просмотр максимального количества вакансий, которое может вернуть сервер по запросу (2000 шт.)
        for num_page in range(20):
            params["page"] = num_page
            list_vacancy.extend(requests.get(self.host, params=params).json()["items"])

        # валидация данных поля 'salary'
        for vac in list_vacancy:
            if vac['salary'] is None:
                sal = "0"
                curr = ""
            else:
                if vac['salary']['from'] is None:
                    _from = 0
                else:
                    _from = vac['salary']['from']
                if vac['salary']['to'] is None:
                    _to = 0
                else:
                    _to = vac['salary']['to']
                sal = str(max(_from, _to))
                curr = vac['salary']['currency']

            # форматируем вакансию для передачи в выходной список
            if vacancy_city is None or vac['area']['name'] == vacancy_city.capitalize():
                vac_dict = dict(id=vac['id'],
                                name=vac['name'],
                                city=vac['area']['name'],
                                description=vac['professional_roles'][0]['name'],
                                salary=sal,
                                currency=curr,
                                url=vac['alternate_url'])
                # формируем выходной список
                out_list_vacancy.append(vac_dict)

        return out_list_vacancy
