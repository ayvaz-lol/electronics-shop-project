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
