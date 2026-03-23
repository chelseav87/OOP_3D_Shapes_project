from shapes import Shapes3D, SquarePyramid, Icosahedron

egg = Shapes3D("some type", "some colour", [1, 2 , 3])
print(egg.getType())
print(f"volume {egg.volume()}, surface area {egg.surface_area()}, {egg.getColour()} {egg.getType()}")
pizza = SquarePyramid("another colour", [1, 2 , 3], 2, 4)
print(pizza.getType())
print(f"volume {pizza.volume()}, surface area {pizza.surface_area()}")
bird = Icosahedron("another colour", [1, 2 , 3], 3)
print(bird.getType())
print(f"volume {bird.volume()}, surface area {bird.surface_area()}")