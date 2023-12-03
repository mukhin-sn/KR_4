class Vacancy:
    """Класс для работы с вакансиями"""

    def __init__(self, data: dict):
        self.data = data
        self.salary = int(data["salary"])

    @classmethod
    def __verify_date(cls, other):
        if not isinstance(other, (int, Vacancy)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")

        return other if isinstance(other, int) else other.salary

    def __lt__(self, other):
        sal = self.__verify_date(other)
        return self.salary < sal

    def __repr__(self):
        return f"{__class__.__name__}: Данные по вакансии - {self.data}"

    def __str__(self):
        out_messages = "\n".join([": ".join([key, value]) for key, value in self.data.items()])
        return f"{out_messages}\n{'-' * 50}"
