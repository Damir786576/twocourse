import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def product_samsung():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def product_iphone():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture()
def product_xiomi():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture()
def product_tv():
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture()
def category1(product_samsung, product_iphone, product_xiomi):
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации," " но и получения дополнительных функций для удобства жизни",
    )
    category.add_product(product_samsung)
    category.add_product(product_iphone)
    category.add_product(product_xiomi)
    return category


@pytest.fixture()
def category2(product_tv):
    category = Category(
        "Телевизоры",
        "Современный телевизор, " "который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    )
    category.add_product(product_tv)
    return category


def test_smartphone(category1):
    assert category1.name == "Смартфоны"
    assert category1.description == (
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни"
    )
    assert len(category1.products) == 3


def test_category_count(category1, category2):
    assert Category.category_count == 2


def test_product_count(category1, category2):
    assert Category.product_count == 4


def test_product_lists(category1):
    product_list = category1.product_lists
    assert product_list.count("Samsung Galaxy S23 Ultra") == 1
    assert product_list.count("Iphone 15") == 1
    assert product_list.count("Xiaomi Redmi Note 11") == 1


def test_add_product(category1, product_tv):
    category1.add_product(product_tv)
    assert len(category1.products) == 4
    assert Category.product_count == 5
