class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'({self.name}, {self.weight}, {self.category})'


class Shop:
    def __init__(self, file_name='products.txt'):
        self.__file_name = file_name

    def get_products(self):
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            products = file.readlines()
        line = ""
        for product in products:
            line += product

        return line

    def add(self, *products):
        existing_product_names = []

        with open(self.__file_name, 'r', ) as file:
            existing_product_names = [line.split(',')[0] for line in file.readlines()]

        with open(self.__file_name, 'w', encoding='utf-8') as file:
            for product in products:
                if product.name in existing_product_names:
                    file.write(f'Продукт {product.name} уже есть в магазине\n')

                else:
                    file.write(f'{product.name}, {product.weight}, {product.category}\n')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
