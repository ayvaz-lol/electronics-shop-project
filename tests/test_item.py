# tests / test_item.py
from src.item import Item


def test_total_cost():
    item = Item("apple", 1.5, 10)
    assert item.get_total_cost() == 15.0


def test_apply_discount():
    Item.discount_level = 0.8
    item = Item("apple", 1.5, 10)
    item.apply_discount()
    assert item.price == 1.2


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('5.6') == 6

def test_initiate_read_cvs():
    items_csv_path = '../src/items.csv'  # Путь к файлу csv
    Item.instantiate_from_csv(items_csv_path)  # создание объектов из данных файла
    assert len(Item.all) == 5
