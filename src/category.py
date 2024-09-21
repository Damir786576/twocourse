from src.product import Product


class Category:
    """Класс для категории"""

    category_count = 0
    product_count = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return self.__products

    @property
    def product_lists(self):
        product_list = []
        for product in self.__products:
            product_info = f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.'
            product_list.append(product_info)
        return '\n'.join(product_list)


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )

    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)
    category2.add_product(product4)
    print(category1.name)
    print(category1.description)
    print(category1.product_lists)
    print(Category.category_count)
    print(Category.product_count)
