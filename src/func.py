import requests
import json
import os


def user_interaction():
    return None


def out_question(question: str, answers: dict):
    """
    Метод вывода вопроса пользователю
    :param question: вопрос пользователю
    :param answers: словарь с вариантами ответов
    """
    print(question)
    print('=' * 50)
    for key in answers:
        print(f"{key} - {answers[key]}")
    print('=' * 50)
    print("Введите номер выбранного варианта")
    print('=' * 50)


def out_open_ended_question(question: str):
    """
    Метод вывода вопроса пользователю без вариантов ответов
    :param question: вопрос пользователю
    """
    print(question)
    print('=' * 50)
    print("Введите запрос")
    print('=' * 50)


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

# country_id = "113"
# url_var = 'https://api.hh.ru/vacancies/' # 'https://api.hh.ru/areas/'
# url_var = 'https://api.superjob.ru/2.0/vacancies/'
#
# param = {"Host": "api.superjob.ru",
#         "X-Api-App-Id": os.getenv('SJ_API_KEY'),
#         "Content-Type": "application/x-www-form-urlencoded"}

# response = requests.get(url_var, headers={"User-Agent": "python-requests/2.31.0"}, params={"page": 0, "per_page": 2}) #headers={"User-Agent": "MyApp/1.0"}

# response = requests.get(url_var, headers={"X-Api-App-Id": os.getenv('SJ_API_KEY')})
# response = requests.get(url_var, params={"text": "NAME:Python"})
# print(os.getenv('SJ_API_KEY'))

# print(response.text)

# data = response.content.decode()

# json_data = response.json()
# for i in json_data["items"]:
#     print(i)
# print(json_data["items"][10])

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
#             if len(k['areas'][i]['areas']) != 0:                      # Если у зоны есть внутренние зоны
#                 for j in range(len(k['areas'][i]['areas'])):
#                     areas.append([k['id'],
#                                   k['name'],
#                                   k['areas'][i]['areas'][j]['id'],
#                                   k['areas'][i]['areas'][j]['name']])
#             else:                                                                # Если у зоны нет внутренних зон
#                 areas.append([k['id'],
#                               k['name'],
#                               k['areas'][i]['id'],
#                               k['areas'][i]['name']])
#     # print(js_obj)
#     return areas
#
#
# areas = get_areas()
# print(len(areas))
# # print(areas)
# for i in areas:
#     print(f"{i[0]} - {i[1]}, {i[2]} - {i[3]}")
