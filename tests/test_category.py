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
def category1(product_samsung, product_iphone, product_xiomi):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации," " но и получения дополнительных функций для удобства жизни",
        [product_samsung, product_iphone, product_xiomi],
    )


@pytest.fixture()
def product_tv():
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture()
def category2(product_tv):
    return Category(
        "Телевизоры",
        "Современный телевизор, " "который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product_tv],
    )


def test_smartphone(category1):
    assert category1.name == "Смартфоны"
    assert category1.description == (
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни"
    )
    assert len(category1.products) == 3


def test_category_count(category1, category2):
    assert category1.category_count == 3
    assert category2.category_count == 3


def test_product_count(category1, category2):
    assert category1.product_count == 11
    assert category2.product_count == 11
