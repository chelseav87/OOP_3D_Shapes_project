class Shapes3D:
    def __init__(self, type, colour, location):
        self.__shape_type = type
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

class SquarePyramid(Shapes3D):
    def __init__(self, colour, location, base_length, height, slant_height):
        super().__init__("Square-based Pyramid", colour, location)
        self.__base_length = base_length
        self.__height = height
        self.__slant_height = slant_height

    def volume(self):
        pass

    def surface_area(self):
        pass

    def draw(self):
        pass

# class PentagrammicPrism(Shapes3D):
#     pass