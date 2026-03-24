class Shapes3D:
    def __init__(self, shape_type, colour, location):
        self.__shape_type = shape_type
        self.__shape_colour = colour
        self.__shape_location = location

    def volume(self):
        return None

    def surface_area(self):
        return None

    def draw(self):
        return None

    def getType(self):
        return self.__shape_type

    def getColour(self):
        return self.__shape_colour

    def setColour(self, new_colour):
        self.__shape_colour = new_colour

    def getLocation(self):
        return self.__shape_location

    def setLocation(self, new_location):
        self.__shape_location = new_location

class SquarePyramid(Shapes3D):
    def __init__(self, colour, location, base_length, height):
        super().__init__("Square-based Pyramid", colour, location)
        self.__base_length = base_length
        self.__height = height

    def volume(self):
        return 1/3 * self.__base_length ** 2 * self.__height

    def surface_area(self):
        return self.__base_length ** 2 + 2 * self.__base_length * (self.__base_length ** 2 / 4 + self.__height ** 2) ** 0.5

    def draw(self):
        pass

class Icosahedron(Shapes3D):
    def __init__(self, colour, location, side_length):
        super().__init__("Icosahedron", colour, location)
        self.__side_length = side_length

    def volume(self):
        return (5 * (3 + 5 ** 0.5))/12 * self.__side_length ** 3

    def surface_area(self):
        return 5 * 3 ** 0.5 * self.__side_length ** 2

    def draw(self):
        pass