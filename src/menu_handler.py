from src.vacancy import *
from src.api_handler import *


class MenuHandler:
    """
    Класс для работы с меню программы парсинга сайтов
    hh.ru и superjob.ru
    """
    def __init__(self, hh_api: HHruAPI, sj_api: SuperJobAPI, data_file: JSONSaver):

        self.menu_1 = {"1": "Работа с запросами",
                       "2": "Работа с файлом",
                       "3": "Выход из программы",
                       }

        self.menu_2 = {"1": "Запрос на HeadHunter",
                       "2": "Запрос на SuperJob",
                       "3": "Запрос на HeadHunter и SuperJob",
                       "4": "Новый запрос, без сохранения результатов",
                       "5": "Найти в найденном",
                       "6": "Вывести ТОП-10 результатов поиска по зарплате",
                       "7": "Сохранить результат запроса (будете перенаправлены в меню работы с файлом)",
                       "8": "Возврат в основное меню",
                       }

        self.menu_3 = {"1": "Сохранить результат в файл (файл будет перезаписан новыми данными)",
                       "2": "Добавить результат в файл",
                       "3": "Найти в файле",
                       "4": "Найти в найденном",
                       "5": "Удалить из файла",
                       "6": "Вывести содержимое файла на экран",
                       "7": "Выйти в меню запросов",
                       }

        self.answers_list = {"1": "да", "2": "нет"}
        self.hh_api = hh_api
        self.sj_api = sj_api
        self.data_file = data_file
        self.vacancy = []
        self.city_vacancy = None
        self.answer = ""

    def out_message(self, text: str):
        """
        Метод вывода сообщения
        :param text: содержит текст сообщения
        :return: None
        """
        print(f"\n{text}\n{'-' * 50}")

    def out_question(self, question: str, answers: dict):
        """
        Метод вывода вопроса пользователю
        :param question: - вопрос пользователю
        :param answers: - словарь с вариантами ответов
        """
        print(f"\n{question}\n{'-' * 50}")
        for key in answers:
            print(f"{key} - {answers[key]}")
        self.out_message("Введите номер выбранного варианта")

    def input_answer(self):
        """
        Метод ввода ответа на запрос
        :return:
        """
        answer = input("-> ")
        return answer

    def check_answer(self, answer: str, answer_options: dict) -> bool:
        """
        Метод проверки ответа пользователя
        :param answer: - ответ пользователя
        :param answer_options: - допустимые варианты ответов
        :return: - True, если 'answer' есть в 'answer_options'
        """
        if answer in answer_options:
            return True
        return False

    def output_on_display(self, data: list) -> None:
        """
        Метод вывода на экран элементов списка вакансий,
        полученных в результате запроса
        :param data: - список вакансий (в нашем случае - список словарей)
        :return: None
        """
        temp_list = []
        for dic_data in data:
            for key, value in dic_data.items():
                temp_list.append(": ".join([key, value]))
            print(", ".join(temp_list))
            temp_list = []

    def question_handler(self, answer_options: dict) -> str:
        """
        Метод обработки ответа на вопрос
        зацикливается, пока не будет введен существующий вариант,
        соответствущий ключу словаря с вариантами ответов.

        :param answer_options: - словарь с вариантами ответов
        :return: - ключ словаря, соответствующий ответу пользователя
        """
        answer = ""
        while not self.check_answer(answer, answer_options):
            answer = self.input_answer()
            if self.check_answer(answer, answer_options):
                return answer
            print("Такого варианта нет. Введите существующий вариант")
            continue

    def top_10(self, data: list) -> list:
        """
        Метод вывода ТОП-10 вакансий. Работает с классом 'Vacancy'
        Если общее количество вакансий меньше 10, то выводит все
        :param data: - список данных с вакансиями (список словарей)
        :return: - список со словарями ТОП-10 вакансий
        """
        try:
            vac_obj_lst = []
            for vac in data:
                vacancy = Vacancy(vac)
                vac_obj_lst.append(vacancy)

            # Сортируем вакансии в списке по зарплате
            v_top = sorted(vac_obj_lst, reverse=True)

            # Проверка количества вакансий в списке
            if len(vac_obj_lst) > 10:
                top_list = v_top[:10]
            else:
                top_list = v_top

            # Вывод на экран ТОП-листа
            print("=" * 50)
            for i in top_list:
                print(f"id: {i.data['id']}, "
                      f"{i.data['name']}, "
                      f"зарплата: {i.data['salary']} "
                      f"{i.data['currency']}")

            # Формирования выходного списка (для сохранения в файл)
            out_list = []
            for obj in top_list:
                out_list.append(obj.data)
            return out_list

        except TypeError:
            print("Неверный формат данных")

    def search_handler(self, data_list: list, search_query: str) -> list:
        """
        Метод поиска в списке данных по запросу
        :param data_list: - список данных, в котором производится поиск
        :param search_query: - строка для поиска в списке
        :return: - список с элементами, удовлетворяющими запросу
        """
        out_list = []
        for dic_i in data_list:
            for key in dic_i:
                if search_query.lower() in dic_i[key].lower():
                    out_list.append(dic_i)
                    break
        return out_list

    def menu_three_handler(self):
        """
        Метод обработки menu_3
        """
        while True:
            self.out_question("Сделайте выбор", self.menu_3)
            self.answer = self.question_handler(self.menu_3)
            if self.answer == "7":
                if self.vacancy:
                    self.out_question("Есть не сохраненные данные.\nСохранить?",
                                      self.answers_list)
                    answer_two = self.question_handler(self.answers_list)
                    if answer_two == "1":
                        continue
                break
            elif self.answer == "1":
                self.data_file.save_vacancy(self.vacancy)
                self.out_message("Данные сохранены в файл")
                self.vacancy = []
            elif self.answer == "2":
                self.data_file.add_vacancy(self.vacancy)
                self.out_message("Данные добавлены в файл")
                self.vacancy = []
            elif self.answer == "3":
                self.out_message("Введите поисковый запрос")
                search_query = self.input_answer()
                self.vacancy = self.data_file.get_vacancy(search_query)
                self.output_on_display(self.vacancy)
            elif self.answer == "4":
                self.out_message("Введите поисковый запрос")
                search_query = self.input_answer()
                self.vacancy = self.search_handler(self.vacancy, search_query)
                self.output_on_display(self.vacancy)
            elif self.answer == "5":
                self.out_message("Введите поисковый запрос для удаления")
                search_query = self.input_answer()
                self.vacancy = self.data_file.get_vacancy()
                self.vacancy = self.search_handler(self.vacancy, search_query)
                self.out_message("Эти данные будут удалены.")
                self.output_on_display(self.vacancy)
                input("Для удаления нажмите любую клавишу")
                self.data_file.del_vacancy(search_query)
            else:
                self.vacancy = self.data_file.get_vacancy()
                self.output_on_display(self.vacancy)

    def menu_two_handler(self):
        """
        Метод обработки menu_2
        """
        while True:
            self.out_question("Сделайте выбор", self.menu_2)
            self.answer = self.question_handler(self.menu_2)
            if self.answer == "8":
                break
            elif self.answer in ("1", "2", "3"):
                self.out_message("Введите поисковый запрос - название вакансии")
                vac_name = self.input_answer()
                self.out_question("Хотите выполнить поиск вакансий в каком-то конкретном городе?",
                                  self.answers_list)
                answer_two = self.question_handler(self.answers_list)
                if answer_two == "1":
                    self.out_message("Введите название города для поиска вакансий")
                    self.city_vacancy = self.input_answer()
                    self.out_message("Пожалуйста подождите.\nОбработка запроса займет некоторое время")
                    if self.answer == "1":
                        self.vacancy = self.hh_api.api_handler(vac_name, self.city_vacancy)
                        self.output_on_display(self.vacancy)
                    elif self.answer == "2":
                        self.vacancy = self.sj_api.api_handler(vac_name, self.city_vacancy)
                        self.output_on_display(self.vacancy)
                    else:
                        self.vacancy = self.hh_api.api_handler(vac_name, self.city_vacancy)
                        self.vacancy.extend(self.sj_api.api_handler(vac_name, self.city_vacancy))
                        self.output_on_display(self.vacancy)
            elif self.answer == "4":
                self.vacancy = []
                continue
            elif self.answer == "5":
                print()
                self.out_message("Введите поисковый запрос")
                search_query = self.input_answer()
                self.vacancy = self.search_handler(self.vacancy, search_query)
                self.output_on_display(self.vacancy)
            elif self.answer == "6":
                if not len(self.vacancy):
                    self.out_message("Отсутствуют результаты для вывода")
                    continue
                else:
                    self.vacancy = self.top_10(self.vacancy)
            else:
                self.menu_three_handler()

    def menu_one_handler(self):
        """
        Метод обработки menu_1 - основного меню программы
        """
        while True:
            self.out_question("Сделайте выбор", self.menu_1)
            self.answer = self.question_handler(self.menu_1)
            if self.answer == "3":
                quit("Выход из программы")
            elif self.answer == "1":
                self.menu_two_handler()
            else:
                self.menu_three_handler()
