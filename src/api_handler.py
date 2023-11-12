from abc import ABC, abstractmethod
import requests
import os


class APIHandler(ABC):
    """Абстрактный класс для работы с API сайтов"""

    @abstractmethod
    def api_handler(self):
        """Абстрактный метод для работы с API сайтов"""
        pass


class SuperJobAPI(APIHandler):
    """Класс для работы с API сайта superjob.ru"""

    def __init__(self, **kwargs):
        self.host = 'https://api.superjob.ru/2.0/vacancies/'
        self.api_key = os.getenv('SJ_API_KEY')
        self.params = kwargs
        self.head = {"X-Api-App-Id": self.api_key}
        self.resp = requests.get(self.host, headers=self.head, params=self.params).json()
        # print(self.resp)

    def __str__(self):
        return self.api_key

    def api_handler(self):
        pass


class HHruAPI(APIHandler):
    """Класс для работы с API сайта hh.ru"""

    def __init__(self, **kwargs):
        self.host = 'https://api.hh.ru/vacancies/'
        self.params = kwargs
        self.resp = requests.get(self.host, params=self.params).json()
        # print(self.resp)

    def api_handler(self):
        pass


#####################################################################################################################
# obj_1 = SuperJobAPI()
obj_2 = HHruAPI()
# print(obj_1)
