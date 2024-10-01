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
        if type(self) == type(other):
            total_sum = (self.price * self.quantity) + (other.price * other.quantity)
            return total_sum
        raise TypeError


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
