from src.item import Item
import os.path


if __name__ == '__main__':
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'Смартфон'
    # Exception: Длина наименования товара превышает 10 символов.
    items_csv_path = 'items.csv'
    print(os.path.exists(items_csv_path))
    Item.instantiate_from_csv(items_csv_path)  # создание объектов из данных файла
    print(Item.instantiate_from_csv(items_csv_path))
    assert len(Item.all) == 5 # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
