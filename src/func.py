import requests
import json


url_var = 'https://api.hh.ru/vacancies/'
response = requests.get(url_var, params={"page": 0, "per_page": 100})
# data = response.content.decode()

json_data = response.json()
# print(type(json_data))
# j_data = json.loads(json_data)
# print(j_data)

print(len(json_data["items"]))
for i in range(len(json_data["items"])):
    print(json_data["items"][i]["name"])
# for key in json_data['name']:
#     print(key)

# print(len(json_data))
# print(response.text)
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
