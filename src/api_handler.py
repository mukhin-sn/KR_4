from abc import ABC, abstractmethod


class APIHandler(ABC):
    """Абстрактный класс для работы с API сайтов"""
    @abstractmethod
    def api_handler(self):
        """Абстрактный метод для работы с API сайтов"""
        pass


class SuperJobAPI(APIHandler):
    """Класс для работы с API сайта superjob.ru"""
    def __init__(self):
        pass

    def api_handler(self):
        pass


class HhRuAPI(APIHandler):
    """Класс для работы с API сайта hh.ru"""
    def __init__(self):
        pass

    def api_handler(self):
        pass
