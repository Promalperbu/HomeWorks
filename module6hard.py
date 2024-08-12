class Figure:
    def __init__(self, sides_count = 0, __sides, __color,  filled ):
        self.side_count = sides_count
        self.__sides = __sides
        self.__color = __color
        self.filled = filled
    def get_color(self):
        return __color


    def __is_valid_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        if self.r


    def set_color(self):


    def __is_valid_sides(self):


    def get_sides(self):


    def __len__(self):


    def set_sides(self, *new_sides):


class Circle(Figure):
    def __init__(self, sides_count = 1, __radius):
        self.side_count = sides_count
        self.__radius = __radius
    def get_square(self):


class Triangle(Figure):
    def __init__(self, sides_count = 3, __height):
        self.side_count = sides_count
        self.__height = __height
    def get_square(self):



class Cube(Figure):
    def __init__(self, sides_count = 12):
        self.side_count =sides_count

    def get_volume(self):





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
