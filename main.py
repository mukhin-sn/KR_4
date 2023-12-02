from src.func import *
# from src.api_handler import *
# from src.file_handler import *

"""
Программа поиска вакансий на сайтах 'superjob.ru' и/или 'hh.ru'
с возможностью сортировки по зарплате
"""

menu_1 = {"1": "HeadHunter",
          "2": "SuperJob",
          "3": "HeadHunter и SuperJob",
          "4": "Выход из программы",
          }

menu_2 = {"1": "Сохранить результат в файл?",
          "2": "Добавить результат в файл?",
          "3": "Вывести результат на экран?",
          "4": "Вывести на экран ТОП-10 вакансий по зарплате?",
          "5": "Сформировать новый запрос?",
          "6": "Выйти в главное меню"
          }

answers_list = {"1": "да", "2": "нет"}
answer = ""
vacancy_city = None

if __name__ == '__main__':

    hh_api = HHruAPI()
    sj_api = SuperJobAPI()
    data_file = JSONSaver("src/json_data.json")

    while True:
        print("-" * 50)
        out_question("К какой платформе хотите выполнить запрос?", menu_1)
        answer = question_handler(menu_1)
        # while not check_answer(answer, platforms):
        #     answer = input_answer()
        #     if check_answer(answer, platforms):
        #         break
        #     print("Такого варианта нет. Введите существующий вариант")
        #     continue
        if answer == "4":
            quit("Выход из программы")

        while True:
            out_message("Запрос по какой вакансии Вы хотите сформировать?")
            out_message("Введите запрос")
            vacancy_name = input_answer()
            out_question("Хотите выполнить поиск вакансий в каком-то конкретном городе?",
                         answers_list)
            answer_two = question_handler(answers_list)
            if answer_two == "1":
                out_message("Введите название города для поиска вакансий")
                vacancy_city = input_answer()
            out_message("Пожалуйста подождите.\nОбработка запроса займет некоторое время")

            if answer == "1":
                vacancy = hh_api.api_handler(vacancy_name, vacancy_city)
            elif answer == "2":
                vacancy = sj_api.api_handler(vacancy_name, vacancy_city)
            else:
                vacancy = hh_api.api_handler(vacancy_name, vacancy_city)
                vacancy.append(sj_api.api_handler(vacancy_name, vacancy_city))

            out_question("Что хотите сделать с результатом запроса?", menu_2)
            answer = question_handler(menu_2)

            while True:
                if answer == "5":
                    continue
                elif answer == "1":
                    data_file.save_vacancy(vacancy)
                elif answer == "2":
                    data_file.add_vacancy(vacancy)
                elif answer == "3":
                    output_on_display(vacancy)
                elif answer == "4":
                    vacancy = top_10(vacancy)
                elif answer == "6":
                    break
                print()

                out_question("Сделать дополнительный поиск "
                             "в полученом результате?",
                             answers_list)
                answer_two = question_handler(answers_list)

                if answer_two == "1":
                    out_message("Введите поисковый запрос")
                    search_query = input_answer()

                else:
                    out_question("Что хотите сделать с результатом запроса?", menu_2)
                    answer = question_handler(menu_2)
                    continue

    # print(check_answer(answer, platforms))
    # out_question("Продолжить?", answers_list)
    # answer = input_answer()
    # print(check_answer(answer, answers_list))

    # while True:
    #
    #     # Первый вопрос
    #     answer = question_to_user("Запрос к какой платформе хотите выполнить", platform, flag=True)
    #     if answer:
    #         print("Продолжаем")
    #         pass
    #     else:
    #         answer_2 = question_to_user("Такого варианта нет. Продолжить?", answers_lst)
    #         while not answer_2:
    #             answer_2 = question_to_user("Такого варианта нет. Продолжить?", answers_lst)
    #             continue
    #         # print(f"{answers_lst[int(answer_2) - 1]}")
    #         if answer_2 == str("2"):
    #             print("Конец работы")
    #             break
    #
    #     # Второй вопрос
    #     search_query = question_to_user("Введите название вакансии", flag=False)
    #     print(search_query)
