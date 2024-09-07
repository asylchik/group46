class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length**2

    def info(self):
        print(f'Square side length: {self.__side_length}{self.unit}, area: {self.calculate_area()}{self.unit}.')


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        print(f'Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit},  area: {self.calculate_area()}{self.unit}.')


figure_list = [Square(4), Square(7), Rectangle(3, 5), Rectangle(4, 6), Rectangle(7, 8)]
for i in figure_list:
    i.info()