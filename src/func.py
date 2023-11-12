import requests
import json
import os


url_var = 'https://api.hh.ru/vacancies/'
# url_var = 'https://api.superjob.ru/2.0/vacancies/'

# param = {"Host": "api.superjob.ru",
#         "X-Api-App-Id": os.getenv('SJ_API_KEY'),
#         "Content-Type": "application/x-www-form-urlencoded"}

response = requests.get(url_var, headers={"User-Agent": "python-requests/2.31.0"}, params={"page": 0, "per_page": 2}) #headers={"User-Agent": "MyApp/1.0"}
# response = requests.get(url_var, headheaders={"User-Agent":={"X-Api-App-Id": os.getenv('SJ_API_KEY')})

print(response.text)

# data = response.content.decode()

# json_data = response.json()
# print(json_data)

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
print(response.request.headers)

# response = requests.get('https://httpbin.org/basic-auth/foo/bar')
# print(response.status_code)  # 401
# response = requests.get('https://httpbin.org/basic-auth/foo/bar', auth=('foo', 'bar'))
# print(response.status_code)  # 200
# print(response.request.headers['Authorization'])   # 'Basic Zm9vOmJhcg=='

# dict_test = {1: "a", 2: "b", 3: "c", 4: "d"}
# for i in dict_test.items():
#     print(f'{i[0]} - {i[1]}')
#     print()
