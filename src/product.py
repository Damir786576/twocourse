class Product:
    """Класс для продукта"""

    def __init__(self, name, description, price, quantity):
        """Задаем значение атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_str):
        name = product_str.get("name")
        description = product_str.get("description")
        price = product_str.get("price")
        quantity = product_str.get("quantity")
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_product):
        if new_product <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            self.__price = new_product

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт. '

    def __add__(self, other):
        total_sum = (self.price * self.quantity) + (other.price * other.quantity)
        return total_sum


if __name__ == "__main__":
    product1 = {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
                "quantity": 5}
    product2 = {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8}
    product3 = {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14}

    product1 = Product.new_product(product1)
    product2 = Product.new_product(product2)
    product3 = Product.new_product(product3)

    for product in [product1, product2, product3]:
        print(product.name, end=',')
        print(product.description, end=',')
        print(product.price, end=',')
        print(product.quantity, end='\n')
