from shapes import Shapes3D, SquarePyramid

egg = Shapes3D("some type", "some colour", [1, 2 , 3])
print(f"volume {egg.volume()}, surface area {egg.surface_area()}, {egg.getColour()} {egg.getType()}")