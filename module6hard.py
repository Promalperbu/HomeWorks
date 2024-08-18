
import math
class Figure:

    def __init__(self, color, *sides,  filled=False, sides_count = 0):
        self.side_count = sides_count
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        valid_values = 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
        return valid_values


    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

#    @staticmethod
    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides(self):
        if self.__is_valid_sides():
            return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *sides):
        if len(sides) == len(self.__sides):
            valid_sides = []
            for side in sides:
                if self.__is_valid_sides(side):
                    valid_sides.append(side)

            self.__sides = valid_sides
class Circle(Figure):

    def __init__(self, color, sides, filled=False):
        super().__init__(color, sides, filled=filled)
        self.__radius = sides/ (2 * math.pi)

    def get_square(self):
        return self.__radius ** 2 / (4 * math.pi)

class Triangle(Figure):

    def __init__(self, sides_count = 3, *height):
        self.side_count = sides_count
        self.__height = height

    def get_square(self):
        perimetr = 0
        n = len(self.__sides)
        for i in range(0, n - 1):
            perimetr += i
        return perimetr/2



class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple[int, int, int], side, filled=False):
        super().__init__(color, *([side] * 12), filled=filled)



    def get_volume(self):
        return self.get_sides()[0] ** 3





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
