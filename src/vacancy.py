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


###################################################################################################################
# obj_vacancy = Vacancy("Python", "http://qoogle.com", "150 000", "Хороший сайт")
# print(obj_vacancy)
# print(repr(obj_vacancy))

# obj_vacancy = SuperJobAPI()
# vac_obj_lst = []
# list_vacancy = obj_vacancy.api_handler("Python", "Красноярск")

# for i in list_vacancy:
#     print(i)
#     vacancy = Vacancy(i)
#     vac_obj_lst.append(vacancy)
# print("*" * 50)
# # var_dic = list_vacancy[0]
# for i in vac_obj_lst:
#     print(i)


# vacancy = Vacancy(i)
# vacancy = Vacancy(i["name"], i["url"], i["salary"], i["description"])
# vac_obj_lst.append(vacancy)
# print(vacancy)
# print(vac_obj_lst)
# print(len(vac_obj_lst))

# for i in vac_obj_lst:
#     print(f"{i.data['name']}, зарплата: {i.data['salary']}")
#     # print(i)
# v_top = sorted(vac_obj_lst, reverse=True)
# print("=" * 50)
# for i in v_top:
#     # print(i)
#     print(f"{i.data['name']}, зарплата: {i.data['salary']}")
