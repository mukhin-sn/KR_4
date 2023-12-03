from abc import ABC, abstractmethod
import json


class WorkingWithFiles(ABC):
    """
    Абстрактный класс для работы с файлами
    """

    @abstractmethod
    def save_vacancy(self, data: list):
        """
        Абстрактный метод записи данных в файл.
        :param data: - данные, сохраняемые в файл
        """

    @abstractmethod
    def add_vacancy(self, vacancy: list) -> None:
        """
        Абстрактный метод для добавления вакансии в файл
        """
        pass

    @abstractmethod
    def get_vacancy(self, data: str) -> list:
        """
        Абстрактный метод для получения данных о вакансии из файла по определенным критериям
        """
        pass

    @abstractmethod
    def del_vacancy(self, data: str):
        """
        Абстрактный метод для удаления вакансии из файла
        """
        pass


class JSONSaver(WorkingWithFiles):
    """
    Класс, для работы с фйлами JSON
    """

    def __init__(self, filename: str):
        self.filename = filename

    def save_vacancy(self, data=None):
        """
        Метод записи данных в файл.
        Файл при этом перезаписывается
        :param data: данные, сохраняемые в файл (список словарей)
        """
        if data is None:
            data = dict(object=[])
        else:
            data = dict(object=data)
        with open(self.filename, 'w') as file:
            json.dump(data, file)

    def remove_duplicate(self, data: list) -> list:
        """
        Метод удаляет дубликаты записей из списка
        и формирует список для вывода
        :param data: - список, который нужно почистить от дублирующих записей
        :return: - очищенный от дубликатов список
        """

        # Убираем дублирующиеся записи
        new_lst = [dict(s) for s in set(frozenset(fd.items()) for fd in data)]

        # Приводим список словарей к нормальному виду
        temp_list = []
        for i_dict in new_lst:
            temp_dict = dict(id=i_dict["id"],
                             name=i_dict["name"],
                             city=i_dict["city"],
                             description=i_dict["description"],
                             salary=i_dict["salary"],
                             currency=i_dict["currency"],
                             url=i_dict["url"])
            temp_list.append(temp_dict)
        return temp_list

    def add_vacancy(self, vacancy=None):
        """
        Добавляет вакансии (список словарей) в файл
        """
        # Если файл отсутствует, то создаем его с пустым словарем
        if vacancy is None:
            vacancy = []
        try:
            with open(self.filename, "r") as file:
                file.read()
        except FileNotFoundError:
            self.save_vacancy()

        # Если файл не содержит словарь, то перезаписываем его с пустым словарем
        with open(self.filename, "r") as file:
            data = file.read()
            if len(data) < 12 or not (data[0] == "{" and data[-1] == "}"):
                self.save_vacancy()

        # Читаем данные из файла
        with open(self.filename, "r") as file:
            data = json.load(file)
            file_data = data["object"]

            # Добавляем к считанным из файла данным новые
            file_data.extend(vacancy)

        # Убираем дублирующиеся записи и перезаписываем файл с обновленными данными
        self.save_vacancy(self.remove_duplicate(file_data))

    def get_vacancy(self, *args) -> list:
        """
        Возвращает данные из файла, соответствующие критериям *args
        Если args=None - возвращает всё содержимое файла
        :param args: - список для поиска
        :return: - список со словарями, удовлетворяющий поисковому запросу
        """
        out_data = []
        args_list = []
        for i in args:
            if isinstance(i, str):
                args_list.append(i.lower())
        try:
            if len(args) == 0:
                with open(self.filename, "r") as file:
                    file_data = json.load(file)
                return file_data["object"]

            with open(self.filename, "r") as file:
                file_data = json.load(file)
                for vac in file_data["object"]:
                    for key in vac:
                        for i in args_list:
                            if i in vac[key].lower():
                                out_data.append(vac)

                # Убираем дублирующиеся записи
                return self.remove_duplicate(out_data)

        # Если файл не найден - записываем пустой json-файл и возвращаем пустой список
        except FileNotFoundError:
            print("Файл не найден")
            print("будет создан пустой json - файл")
            self.save_vacancy()
            return []

    def del_vacancy(self, data=None):
        """
        Удаляет данные с параметром 'data' из файла
        """
        if not data or data == " ":
            return None

        # Проверяем наличие файла
        try:
            with open(self.filename, "r") as file:
                file.read()

        # Если файл не найден - записываем пустой json-файл
        except FileNotFoundError:
            print("Файл не найден")
            print("будет создан пустой json - файл")
            self.save_vacancy()
            return None

        # Читаем данные из файла
        with open(self.filename, "r") as file:
            file_data = json.load(file)

        # Ищем данные для удаления
        new_lst = []
        is_available = False
        for vac in file_data["object"]:
            for key in vac:

                # Проверяем данные из запроса 'data' в каждом поле словаря
                if data.lower() in vac[key].lower():
                    is_available = True
                    break

            # Если данных не было ни в одном поле словаря,
            # то добавляем его в новый список
            if not is_available:
                new_lst.append(vac)
            is_available = False

        # Сохраняем обновленный список в файл
        self.save_vacancy(new_lst)
