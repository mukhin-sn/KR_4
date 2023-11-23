from abc import ABC, abstractmethod
import requests
import os


class APIHandler(ABC):
    """
    Абстрактный класс для работы с API сайтов
    """

    @abstractmethod
    def api_handler(self, vacancy_name: str):
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

    def api_handler(self, vacancy_name: str) -> list:
        """
        Метод получения списка вакансий, согласно фильтру
        :param vacancy_name: - строка для фильтра
        :return: -> отформатированный по требуемым полям список вакансий
        """
        out_list_vacancy = []
        params = {
            "count": 100,
            "archive": False,
            "keyword": vacancy_name
            # "keywords[0][srws]": 1,
            # "keywords[0][skwc]": "and",
            # "keywords[0][keys]": keys,

            # "keywords": {
            #     "srws": 1,
            #     "skwc": "and",
            #     "keys": keys
            #             }
                  }
        for num_page in range(5):
            params["page"] = num_page
            out_list_vacancy.extend(requests.get(self.host, headers=self.head, params=params).json()["objects"])
        return out_list_vacancy


class HHruAPI(APIHandler):
    """Класс для работы с API сайта hh.ru"""

    def __init__(self):
        self.host = 'https://api.hh.ru/vacancies/'
        self.resp = requests.get(self.host).request.headers

    def __str__(self):
        return ", ".join([f"{key}: {self.resp[key]}" for key in self.resp])

    def api_handler(self, vacancy_name: str) -> list:
        """
        Метод получения списка вакансий в Российском сегменте, согласно фильтру
        :param vacancy_name: - строка для фильтра
        :return: -> отформатированный по требуемым полям список вакансий
        """
        # список, полученных при запросе к сайту, вакансий
        list_vacancy = []

        # список, который будет возвращать функция
        out_list_vacancy = []

        # параметры, передаваемые в GET запросе
        params = {
            "per_page": 100,
            "area": ["113"],
            "text": f"name:{vacancy_name}",
                 }

        # просмотр максимального колличества вакансий, которое может вернуть сервер по запросу (2000 шт.)
        for num_page in range(20):
            params["page"] = num_page
            list_vacancy.extend(requests.get(self.host, params=params).json()["items"])

        # валидация данных поля 'salary'
        for vac in list_vacancy:
            if vac['salary'] is None:
                sal = None
            else:
                sal = {'from': vac['salary']['from'],
                       'to': vac['salary']['to'],
                       'currency': vac['salary']['currency'],
                       }

            # форматируем вакансию для передачи в выходной список
            vac_dict = dict(id=vac['id'],
                            name=vac['name'],
                            profession=vac['professional_roles'][0]['name'],
                            salary=sal,
                            url=vac['alternate_url'])

            # формируем выходной список
            out_list_vacancy.append(vac_dict)
        return out_list_vacancy


#####################################################################################################################
obj_1 = SuperJobAPI()
# print(obj_1)

obj_2 = HHruAPI()
# print(obj_2)
#
lst_vacancy = obj_2.api_handler("Python")
print(len(lst_vacancy))
# for i in lst_vacancy:
#     print(i["profession"])
# print(lst_vacancy[5])
# print(len(lst_vacancy["objects"]))

for i in lst_vacancy:
    print(i)

# for i in lst_vacancy:
#     # print(i["name"])
#     if i['salary'] is None:
#         salary = "зарплата: XXX"
#     else:
#         salary = f"зарплата: от {i['salary']['from']} до {i['salary']['to']})"
#     print(i)
#     print(f"id: {i['id']}, "
#           f"название: {i['name']}, "
#           f"город: {i['area']['name']}, "
#           f"профессия: {i['professional_roles'][0]['name']}, "
#           f"{salary}")
#     print('-' * 50)
# print(lst_vacancy[10])
