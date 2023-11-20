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
obj_vacancy = Vacancy("Python", "http://qoogle.com", "150 000", "Хороший сайт")
print(obj_vacancy)
print(repr(obj_vacancy))
