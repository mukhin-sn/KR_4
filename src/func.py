import requests
import json
import os

country_id = "5"
url_var = 'https://api.hh.ru/vacancies/' # 'https://api.hh.ru/areas/'
# url_var = 'https://api.superjob.ru/2.0/vacancies/'
#
# param = {"Host": "api.superjob.ru",
#         "X-Api-App-Id": os.getenv('SJ_API_KEY'),
#         "Content-Type": "application/x-www-form-urlencoded"}

# response = requests.get(url_var, headers={"User-Agent": "python-requests/2.31.0"}, params={"page": 0, "per_page": 2}) #headers={"User-Agent": "MyApp/1.0"}

# response = requests.get(url_var, headers={"X-Api-App-Id": os.getenv('SJ_API_KEY')})
response = requests.get(url_var, params={"area": country_id})
# print(os.getenv('SJ_API_KEY'))

# print(response.text)

# data = response.content.decode()

json_data = response.json()
for i in json_data["items"]:
    print(i)
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


def get_areas():
    req = requests.get('https://api.hh.ru/areas')
    data = req.content.decode()
    req.close()
    js_obj = json.loads(data)
    areas = []
    for k in js_obj:
        for i in range(len(k['areas'])):
            if len(k['areas'][i]['areas']) != 0:                      # Если у зоны есть внутренние зоны
                for j in range(len(k['areas'][i]['areas'])):
                    areas.append([k['id'],
                                  k['name'],
                                  k['areas'][i]['areas'][j]['id'],
                                  k['areas'][i]['areas'][j]['name']])
            else:                                                                # Если у зоны нет внутренних зон
                areas.append([k['id'],
                              k['name'],
                              k['areas'][i]['id'],
                              k['areas'][i]['name']])
    # print(js_obj)
    return areas


areas = get_areas()
print(len(areas))
# print(areas)
for i in areas:
    print(f"{i[0]} - {i[1]}, {i[2]} - {i[3]}")
