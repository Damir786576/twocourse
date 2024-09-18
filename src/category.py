from src.product import Product


class Category:
    """Класс для категории"""

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации," " но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, " "который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )
    print(category1.name)
    print(category1.description)
    print(category1.products)
    print(Category.category_count)
    print(Category.product_count)
