from shapes import Shapes3D, Pyramid

egg = Shapes3D("circle", "red")
print(f"volume {egg.volume()}, surface area {egg.surface_area()}")
print(f"{egg.getColour()} {egg.getType()}")
egg.setType("square")
egg.setColour("blue")
print(f"{egg.getColour()} {egg.getType()}")