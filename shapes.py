class Shapes3D:
    def __init__(self, type, colour):
        self.__shape_type = type
        self.__shape_colour = colour

    def volume(self):
        return None

    def surface_area(self):
        return None

    def getType(self):
        return self.__shape_type

    def setType(self, new_type):
        self.__shape_type = new_type

    def getColour(self):
        return self.__shape_colour

    def setColour(self, new_colour):
        self.__shape_colour = new_colour

class Pyramid(Shapes3D):
    pass

# class PentagramPrism(Shapes3D):
#     pass