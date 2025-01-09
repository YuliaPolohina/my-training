class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = sides #список сторон (целые числа)
        self.__color = color #список цветов в формате RGB
        self.filled = False #закрашенный, bool

    def get_color(self): #возвращает список RGB цветов
        return self.__color

    def __is_valid_color(self, r, g, b): #принимает параметры r, g, b, который проверяет корректность переданных значений
        self.r = r
        self.g = g
        self.b = b
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b): #принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            return self.__color

    def __is_valid_sides(self, *new_sides): #принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа
        return len(new_sides) == self.sides_count and all(isinstance(i, int) and i > 0 for i in new_sides)

    def get_sides(self): #должен возвращать значение я атрибута __sides
        return self.__sides

    def __len__(self): #должен возвращать периметр фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides): # должен принимать новые стороны, если их количество не равно sides_count
        for j in new_sides:
            if j != self.__is_valid_sides(j):
                self.__sides = list(new_sides)
                return self.__sides

class Circle(Figure):
    sides_count = 1
    __radius = None

    def get_square(self): #возвращает площадь круга
        s = (self.__radius ** 2) * 3.14
        return s

class Triangle(Figure):
    sides_count = 3

    def get_square(self): #возвращает площадь треугольника
        return (self.side ** 2) * (3 ** 0.5) / 4

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        super().__init__([side] * 12, *color)
        self.__sides = [side] * self.sides_count

    def get_volume(self): #возвращает объём куба
        V = self.__sides[0] ** 3
        return V

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
