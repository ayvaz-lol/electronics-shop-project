import csv
import math


class InstantiateCSVError(Exception):
    '''Класс исключения при обработке csv-файла'''
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        """
        self.__name = name  # Название товара
        self.price = price  # Цена за единицу товара
        self.quantity = quantity  # Количество товара в магазине
        self.all.append(self)
        pass

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        '''Проверяет, чтобы длина наименования товара не была более 10 символов,
                    иначе возвращает ошибку'''
        if len(value) > 10:
            raise Exception("Длина наименования товара превышает 10 символов.")
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls, file_path) -> list:
        '''Считывает данные из csv-файла и создает экземпляры класса,
                инициализируя их данными из файла'''
        cls.all = []
        try:
            with open(file_path, newline='', encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                all = []
                for row in reader:
                    if len(row.keys()) == 3:
                        if cls.is_integer(float(row['price'])):
                            row['price'] = int(float(row['price']))
                        if cls.is_integer(float(row['quantity'])):
                            row['quantity'] = int(float(row['quantity']))
                        all.append(cls(row['name'], row['price'], row['quantity']))
                    else:
                        raise InstantiateCSVError
        except FileNotFoundError:
            message = f"Отсутствует файл по указанному пути: {file_path}"
            print(message)
            return message
        except InstantiateCSVError:
            message = f'Файл по указанному пути поврежден: {file_path}'
            print(message)
            return message
        else:
            return all

    @staticmethod
    def string_to_number(number: str):
        number = float(number)
        number = int(number)
        rounded_num = round(number)
        return rounded_num

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

    @classmethod
    def is_integer(cls, param):
        assert type(param) == float
