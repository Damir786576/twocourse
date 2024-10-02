import pytest

from src.product import Product, Smartphone, LawnGrass


@pytest.fixture()
def product_samsung():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_samsung(product_samsung):
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


@pytest.fixture()
def product_iphone():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


def test_iphone(product_iphone):
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8


@pytest.fixture()
def product_xiomi():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


def test_xiomi(product_xiomi):
    assert product_xiomi.name == "Xiaomi Redmi Note 11"
    assert product_xiomi.description == "1024GB, Синий"
    assert product_xiomi.price == 31000.0
    assert product_xiomi.quantity == 14


def test_price_change(product_samsung):
    product_samsung.price = 200000.0
    assert product_samsung.price == 200000.0


def test_str(product_samsung):
    assert str(product_samsung) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт. "


def test_add_products(product_samsung, product_iphone):
    total_sum = product_samsung + product_iphone
    assert total_sum == (product_samsung.price * product_samsung.quantity) + (product_iphone.price *
                                                                              product_iphone.quantity)


def test_lawngrass_product():
    product_lawngrass = LawnGrass("LawnGrass", "Green grass", 500, 10, "USA", 7, "Green")
    assert product_lawngrass.name == "LawnGrass"
    assert product_lawngrass.description == "Green grass"
    assert product_lawngrass.price == 500
    assert product_lawngrass.quantity == 10
    assert product_lawngrass.country == "USA"
    assert product_lawngrass.germination_period == 7
    assert product_lawngrass.color == "Green"


def test_smartphone_product():
    product_smartphone = Smartphone("Smartphone", "256GB, Серый цвет, 200MP камера", 180000.0, 5, "High", "S23 Ultra",
                                    256,
                                    "Gray")
    assert product_smartphone.name == "Smartphone"
    assert product_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone.price == 180000.0
    assert product_smartphone.quantity == 5
    assert product_smartphone.efficiency == "High"
    assert product_smartphone.model == "S23 Ultra"
    assert product_smartphone.memory == 256
    assert product_smartphone.color == "Gray"
