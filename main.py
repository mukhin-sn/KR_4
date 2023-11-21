from src.func import *

platforms = ["HeadHunter", "SuperJob", "HeadHunter и SuperJob"]
answers_lst = ["да", "нет"]

if __name__ == '__main__':
    while True:

        # Первый вопрос
        answer = question_to_user("Запрос к какой платформе хотите выполнить", platforms, flag=True)
        if answer:
            print("Продолжаем")
            pass
        else:
            answer_2 = question_to_user("Такого варианта нет. Продолжить?", answers_lst)
            while not answer_2:
                answer_2 = question_to_user("Такого варианта нет. Продолжить?", answers_lst)
                continue
            # print(f"{answers_lst[int(answer_2) - 1]}")
            if answer_2 == str("2"):
                print("Конец работы")
                break

        # Второй вопрос
        search_query = question_to_user("Введите название вакансии", flag=False)
        print(search_query)
