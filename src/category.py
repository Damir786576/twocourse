class Category:
    """Класс для категории"""

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return self.__products

    @property
    def products(self):
        product_list = []
        for product in self.__products:
            product_info = f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.'
            product_list.append(product_info)
        return product_list
