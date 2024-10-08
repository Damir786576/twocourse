from src.product import Product, Smartphone, LawnGrass


class Category:
    """Класс для категории"""

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        if isinstance(product, (Smartphone, LawnGrass, Product)):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def list_products(self):
        product_list = []
        for product in self.__products:
            product_info = f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.'
            product_list.append(product_info)
        return '\n'.join(product_list)

    @property
    def products(self):
        return self.list_products

    def __str__(self):
        total = sum(product.quantity for product in self.__products)
        return f'{self.name}, количество продуктов: {total} шт.'

    def middle_price(self):
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0
