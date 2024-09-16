import pytest

from src.product import Product


@pytest.fixture()
def product_samsung():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0,
                   5)


def test_samsung(product_samsung):
    assert product_samsung.name == 'Samsung Galaxy S23 Ultra'
    assert product_samsung.description == '256GB, Серый цвет, 200MP камера'
    assert product_samsung.price == '180000.0 руб'
    assert product_samsung.quantity == '5 шт'


@pytest.fixture()
def product_iphone():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


def test_iphone(product_iphone):
    assert product_iphone.name == 'Iphone 15'
    assert product_iphone.description == '512GB, Gray space'
    assert product_iphone.price == '210000.0 руб'
    assert product_iphone.quantity == '8 шт'


@pytest.fixture()
def product_xiomi():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


def test_xiomi(product_xiomi):
    assert product_xiomi.name == 'Xiaomi Redmi Note 11'
    assert product_xiomi.description == '1024GB, Синий'
    assert product_xiomi.price == '31000.0 руб'
    assert product_xiomi.quantity == '14 шт'
