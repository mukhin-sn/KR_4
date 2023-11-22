from src.func import *
from src.api_handler import *
from src.file_handler import *

"""
Программа поиска вакансий на сайтах 'superjob.ru' и/или 'hh.ru'
с возможностью сортировки:
 - по региону;
 - по зарплате;
 - по названию
"""

platform = ["HeadHunter", "SuperJob", "HeadHunter и SuperJob"]
platforms = {"1": "HeadHunter", "2": "SuperJob", "3": "HeadHunter и SuperJob", "4": "Выход из программы"}
answers_lst = ["да", "нет"]
answers_list = {"1": "да", "2": "нет"}
answer = ""


if __name__ == '__main__':

    hh_api = HHruAPI()
    # print(hh_api)

    sj_api = SuperJobAPI()
    # print(sj_api)
    print("=" * 50)

    out_question("К какой платформе хотите выполнить запрос?", platforms)
    while not check_answer(answer, platforms):
        answer = input_answer()
        if check_answer(answer, platforms):
            break
        print("Такого варианта нет. Введите существующий вариант")
        continue
    if answer == "4":
        quit("Выход из программы")
    out_open_ended_question("Запрос по какой вакансии Вы хотите сформировать?")
    vacancy_name = input_answer()
    if answer == "1":
        hh_vacancy = hh_api.api_handler(vacancy_name)
        # print(hh_vacancy)
    elif answer == "2":
        sj_vacancy = sj_api.api_handler(vacancy_name)
    else:
        hh_vacancy = hh_api.api_handler(vacancy_name)
        sj_vacancy = sj_api.api_handler(vacancy_name)



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
