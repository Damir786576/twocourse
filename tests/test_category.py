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
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product_samsung, product_iphone, product_xiomi])
    print(f'fixture category1 category_count: {Category.category_count}')
    print(f'fixture category1 product_count: {Category.product_count}')
    return category


@pytest.fixture()
def category2(product_tv):
    category = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product_tv])
    print(f'fixture category2 category_count: {Category.category_count}')
    print(f'fixture category2 product_count: {Category.product_count}')
    return category


def test_smartphone(category1):
    assert category1.name == "Смартфоны"
    assert category1.description == (
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни"
    )
    assert len(category1.products.split('\n')) == 3


def test_category_count(category1, category2):
    print(f'fixture test_category_count category_count: {Category.category_count}')
    print(f'fixture test_category_count product_count: {Category.product_count}')
    assert Category.category_count == 2


def test_product_count(category1, category2):
    print(f'fixture test_product_count category_count: {Category.category_count}')
    print(f'fixture test_product_count product_count: {Category.product_count}')
    assert Category.product_count == 4


def test_add_product(category1, product_tv):
    category1.add_product(product_tv)
    print(f'fixture test_add_product category_count: {Category.category_count}')
    print(f'fixture test_add_product product_count: {Category.product_count}')
    assert len(category1.products.split('\n')) == 4
    assert Category.product_count == 5
