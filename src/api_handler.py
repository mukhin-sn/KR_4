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
        :return: -> list
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

    def __init__(self,):
        self.host = 'https://api.hh.ru/vacancies/'
        self.resp = requests.get(self.host).request.headers

    def __str__(self):
        return ", ".join([f"{key}: {self.resp[key]}" for key in self.resp])

    def api_handler(self, vacancy_name: str) -> list:
        """
        Метод получения списка вакансий, согласно фильтру
        :param vacancy_name: - строка для фильтра
        :return: -> list
        """
        out_list_vacancy = []
        params = {
            "per_page": 100,
            "area": ["113"],
            "text": f"name:{vacancy_name}",
                 }
        for num_page in range(20):
            params["page"] = num_page
            out_list_vacancy.extend(requests.get(self.host, params=params).json()["items"])
        return out_list_vacancy


#####################################################################################################################
# obj_1 = SuperJobAPI()
# print(obj_1)

obj_2 = HHruAPI()
print(obj_2)

lst_vacancy = obj_2.api_handler("Python")
print(len(lst_vacancy))
# for i in lst_vacancy:
#     print(i["profession"])
# print(lst_vacancy[5])
# print(len(lst_vacancy["objects"]))

for i in lst_vacancy:
    print(i["name"])
    # print(i)
# print(lst_vacancy[10])
