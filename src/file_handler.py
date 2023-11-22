from abc import ABC, abstractmethod
import json


class WorkingWithFiles(ABC):
    """
    Абстрактный класс для работы с файлами
    """

    @abstractmethod
    def add_vacancy(self, vacancy: dict) -> None:
        """
        Абстрактный метод для добавления вакансии в файл
        """
        pass

    @abstractmethod
    def get_vacancy(self, data: str) -> str:
        """
        Абстрактный метод для получения данных о вакансии из файла по определенным критериям
        """
        pass

    @abstractmethod
    def del_vacancy(self, vacancy: str):
        """
        Абстрактный метод для удаления вакансии из файла
        """
        pass


class JSONSaver(WorkingWithFiles):
    """
    Класс, для работы с фйлами JSON
    """
    def __init__(self, filename: str):
        self.filename = filename

    def add_vacancy(self, vacancy: dict):
        """
        Добавляет вакансию (словарь) в файл
        """
        with (open(self.filename, "r") as file):
            data = file.read()
            if data == "":
                file_data = vacancy
            else:
                file_data = json.loads(data)
                file_data.update(vacancy)
            # print(f"{data}")
        with open(self.filename, 'w') as file:
            json.dump(file_data, file)

    def get_vacancy(self, data=""):
        """
        Возвращает данные из файла, соответствующие критериям 'data='
        """
        with (open(self.filename, "r") as file):
            file_data = json.load(file)
            try:
                out_data = file_data[data]
            except KeyError:
                return "Нет таких данных"
            return out_data

    def del_vacancy(self, vacancy: str):
        """
        Удаляет данные с параметром 'vacancy' из файла
        :param vacancy:
        :return:
        """
        with open(self.filename, "r") as file:
            file_data = json.load(file)
            try:
                file_data.pop(vacancy)
            except KeyError:
                return "Нет данных для удаления"
        with open(self.filename, "w") as file:
            json.dump(file_data, file)


#################################################################################################################
# json_data = JSONSaver("json_data.json")
# data_dic_1 = {"1": "A", "2": "B"}
# data_dic_2 = {"3": "C", "4": "D"}
# json_data.add_vacancy(data_dic_2)
# json_data.del_vacancy("2")
# print(json_data.get_vacancy("4"))
