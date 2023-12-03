from src.vacancy import *
from src.api_handler import *


def out_message(text: str):
    """
    Метод вывода сообщения
    :param text: содержит текст сообщения
    :return: None
    """
    print(f"{text}\n{'-' * 50}")


def out_question(question: str, answers: dict):
    """
    Метод вывода вопроса пользователю
    :param question: вопрос пользователю
    :param answers: словарь с вариантами ответов
    """
    print(f"{question}\n{'-' * 50}")
    for key in answers:
        print(f"{key} - {answers[key]}")
    out_message("Введите номер выбранного варианта")
    # print(f"{'=' * 50}\nВведите номер выбранного варианта\n{'=' * 50}")


# def out_open_ended_question(question: str):
#     """
#     Метод вывода вопроса пользователю без вариантов ответов
#     :param question: вопрос пользователю
#     """
#     print(f"\n{question}\n{'=' * 50}")
# print("Введите запрос")
# print('=' * 50)


def input_answer():
    answer = input("-> ")
    return answer


def check_answer(answer: str, answer_options: dict) -> bool:
    """
    Метод проверки ответа пользователя
    :param answer: ответ пользователя
    :param answer_options: допустимые варианты ответов
    :return: True, если 'answer' есть в 'answer_options'
    """
    if answer in answer_options:
        return True
    return False


def output_on_display(data: list) -> None:
    """
    Метод вывода на экран элементов списка вакансий,
    полученных в результате запроса
    :param data: список вакансий (в нашем случае - список словарей)
    :return: None
    """
    temp_list = []
    for dic_data in data:
        for key, value in dic_data.items():
            temp_list.append(": ".join([key, value]))
        print(", ".join(temp_list))
        temp_list = []


def question_handler(answer_options: dict):
    answer = ""
    while not check_answer(answer, answer_options):
        answer = input_answer()
        if check_answer(answer, answer_options):
            return answer
        print("Такого варианта нет. Введите существующий вариант")
        continue


def top_10(data: list) -> list:
    """
    Метод вывода ТОП-10 вакансий.
    Если общее количество вакансий меньше 10, то выводит все
    :param data: список данных с вакансиями (список словарей)
    :return: список со словарями ТОП-10 вакансий
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

        # Формирования выходного списка (если придется сохранять в файл)
        out_list = []
        for obj in top_list:
            out_list.append(obj.data)
        return out_list

    except TypeError:
        print("Неверный формат данных")


def search_handler(data_list: list, search_query: str) -> list:
    """
    Метод поиска в списке данных по запросу
    :param data_list: список данных, в котором производится поиск
    :param search_query: строка для поиска в списке
    :return: список с элементами, удовлетворяющими запросу
    """
    out_list = []
    for dic_i in data_list:
        for key in dic_i:
            if search_query.lower() in dic_i[key].lower():
                out_list.append(dic_i)

    return out_list


def menu_one_handler():
    pass

def user_interaction():
    menu_1 = {"1": "Работа с запросами",
              "2": "Работа с файлом",
              "3": "Выход из программы",
              }

    menu_2 = {"1": "Запрос на HeadHunter",
              "2": "Запрос на SuperJob",
              "3": "Запрос на HeadHunter и SuperJob",
              "4": "Новый запрос, без сохранения результатов",
              "5": "Найти в найденом",
              "6": "Вывести ТОП-10 результатов поиска по зарплате",
              "7": "Сохранить результат запроса (будете перенаправлены в меню работы с файлом)",
              "8": "Возврат в основное меню",
              }

    menu_3 = {"1": "Сохранить результат в файл",
              "2": "Добавить результат в файл",
              "3": "Найти в файле",
              "4": "Найти в найденом",
              "5": "Удалить из файла",
              "6": "Вывести содержимое файла на экран",
              "7": "Выйти в меню запросов",
              }

    answers_list = {"1": "да", "2": "нет"}
    while True:
        pass


################


def question_to_user(question: str, *arg_question: list, flag=True) -> str:
    """
    Метод вывода вопроса пользователю
    :param question: текст вопроса
    :param arg_question: список предлагаемых вариантов ответа
    :param flag: режим взаимодействи с пользователем после вывода вопроса
    :return: ответ пользователя - № варианта ответа
    """
    print(question)
    num_answer_lst = []
    if flag:
        for i in range(len(arg_question[0])):
            print(f"{i + 1} - {arg_question[0][i]}")
            num_answer_lst.append(str(i + 1))
        print("Введите номер выбранного варианта:")
    answer = input("-> ")
    if not flag:
        # print(answer)
        return answer
    elif answer in num_answer_lst:
        # print("ok")
        return answer
    else:
        # print("Такого варианта нет.\nПродолжить?")
        return ""


####################################################################################

# json_saver = JSONSaver("json_data.json")
# data_vac = json_saver.get_vacancy()
# output_on_display(data_vac)
# print(data_vac)
# res_out = search_handler(data_vac, "backend")
# print(res_out)

# obj_vacancy = HHruAPI()
# vac_obj_lst = []
# list_vacancy = obj_vacancy.api_handler("Python", "Москва")
# list_vacancy = 125
# top_ten(list_vacancy)

# country_id = "113"
# url_var = 'https://api.hh.ru/vacancies/' # 'https://api.hh.ru/areas/'
# url_var = 'https://api.superjob.ru/2.0/vacancies/'
#
# param = {"Host": "api.superjob.ru",
#         "X-Api-App-Id": os.getenv('SJ_API_KEY'),
#         "Content-Type": "application/x-www-form-urlencoded"}

# response = requests.get(
#     url_var,
#     headers={"User-Agent": "python-requests/2.31.0"},
#     params={"page": 0, "per_page": 2}
# )   # headers={"User-Agent": "MyApp/1.0"}

# response = requests.get(url_var, headers={"X-Api-App-Id": os.getenv('SJ_API_KEY')})
# response = requests.get(url_var, params={"text": "NAME:Python"})
# print(os.getenv('SJ_API_KEY'))

# print(response.text)
# print("-" * 50)

# data = response.content.decode()

# json_data = response.json()
# for i in json_data["items"]:
#     print(i)
# print(json_data["items"][0])
# print(json_data["objects"][0])

# print(type(json_data))
# j_data = json.loads(json_data)
# print(j_data)

# print(len(json_data["items"]))
# for i in range(len(json_data["items"])):
#     print(json_data["items"][i]["name"])
# for key in json_data['name']:
#     print(key)

# print(len(json_data))
# print(response.text)
# out_dict = response.request.headers
# print(out_dict)
# out_str = ", ".join([key + ": " + out_dict[key] for key in out_dict])
# out_str = ", ".join([f"{key}: {out_dict[key]}" for key in out_dict])
# print(out_str)
# print(response.request.headers)

# response = requests.get('https://httpbin.org/basic-auth/foo/bar')
# print(response.status_code)  # 401
# response = requests.get('https://httpbin.org/basic-auth/foo/bar', auth=('foo', 'bar'))
# print(response.status_code)  # 200
# print(response.request.headers['Authorization'])   # 'Basic Zm9vOmJhcg=='

# dict_test = {1: "a", 2: "b", 3: "c", 4: "d"}
# for i in dict_test.items():
#     print(f'{i[0]} - {i[1]}')
#     print()


# def get_areas():
#     req = requests.get('https://api.hh.ru/areas')
#     data = req.content.decode()
#     req.close()
#     js_obj = json.loads(data)
#     areas = []
#     for k in js_obj:
#         for i in range(len(k['areas'])):
#             if len(k['areas'][i]['areas']) != 0:  # Если у зоны есть внутренние зоны
#                 for j in range(len(k['areas'][i]['areas'])):
#                     areas.append([k['id'],
#                                   k['name'],
#                                   k['areas'][i]['areas'][j]['id'],
#                                   k['areas'][i]['areas'][j]['name']])
#             else:  # Если у зоны нет внутренних зон
#                 areas.append([k['id'],
#                               k['name'],
#                               k['areas'][i]['id'],
#                               k['areas'][i]['name']])
#     # print(js_obj)
#     return areas
#
#
# areas = get_areas()
# areas_dict = {}
# print(len(areas))
# print(areas)
# for i in areas:
#     print(f"{i[0]} - {i[1]}, {i[2]} - {i[3]}")
# areas_dict = dict([i[3], i[2]])
# print(f"{areas_dict[i[3]]} - ")
