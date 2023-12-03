from src.menu_handler import *

if __name__ == '__main__':

    hh_api = HHruAPI()
    sj_api = SuperJobAPI()
    data_file = JSONSaver("src/json_data.json")

    menu_handler = MenuHandler(hh_api, sj_api, data_file)
    menu_handler.menu_one_handler()
