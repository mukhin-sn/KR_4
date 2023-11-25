from src.func import *
from src.api_handler import *
from src.file_handler import *


class Vacancy:
    """Класс для работы с вакансиями"""
    def __init__(self, vacancy_name: str, vacancy_url: str, salary: str, description: str) -> None:
        self.vacancy_name = vacancy_name
        self.vacancy_url = vacancy_url
        self.salary = salary
        self.description = description

    def __str__(self):
        return f"{__class__.__name__}: вакансия - {self.vacancy_name}"

    def __repr__(self):
        return (f"{self.vacancy_name}\n"
                f"{self.vacancy_url}\n"
                f"{self.salary}\n"
                f"{self.description}\n")

###################################################################################################################
# obj_vacancy = Vacancy("Python", "http://qoogle.com", "150 000", "Хороший сайт")
# print(obj_vacancy)
# print(repr(obj_vacancy))


obj_hhru = HHruAPI()
vac_obj_lst = []
list_vacancy = obj_hhru.api_handler("Python", "Новосибирск")
for i in list_vacancy:
    vacancy = Vacancy(i["name"], i["url"], i["salary"], i["profession"])
    vac_obj_lst.append(vacancy)
    # print(vacancy)
print(vac_obj_lst)
