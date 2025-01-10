class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name #название продукта
        self.weight = weight #общий вес товара
        self.category = category #категория товара

    def __str__(self):
        prods_str = str(f"{self.name}, {self.weight}, {self.category}") #возвращает строку в формате '<название>, <вес>, <категория>'.
        return prods_str

class Shop:
    def __init__(self):
        self.__file_name = open('products.txt', 'a')
        self.__file_name.close()

    def get_products(self): # считывает всю информацию из файла __file_name, закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
        get_file = open('products.txt', 'r')
        name_prod = get_file.read()
        get_file.close()
        return name_prod

    def add(self, *products): #принимает неограниченное количество объектов класса Product. Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
        for product in products:
            if str(product) not in self.get_products():
                file = open('products.txt', 'a+')
                file.write(f'{str(product)}\n')
                file.close()
            else:
                print(f'Продукт {product} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
