from shapes import SquarePyramid, Icosahedron
import tkinter as tk

# --- Input Window --- #
root = tk.Tk()
root.title("3D Shapes App")
root.geometry("280x300")
root.resizable(width=False, height=False)

# Dropdown of 3D Shapes
shapes_list = ["Square-based Pyramid", "Icosahedron"]
shape_prompt = tk.StringVar(value="Choose a 3D shape!")
tk.OptionMenu(root,shape_prompt,*shapes_list).place(x=10, y=10)

# RGB Colour Values
tk.Label(root,text="(Colour)",font=("Arial",9,"bold")).place(x=10,y=50)

red_lbl = tk.Label(root,text="R: ")
red_lbl.place(x=70,y=50)
red_entry = tk.Entry(root,width=4)
red_entry.place(x=90,y=51)

green_lbl = tk.Label(root,text="G: ")
green_lbl.place(x=130,y=50)
green_entry = tk.Entry(root,width=4)
green_entry.place(x=150,y=51)

blue_lbl = tk.Label(root,text="B: ")
blue_lbl.place(x=190,y=50)
blue_entry = tk.Entry(root,width=4)
blue_entry.place(x=210,y=51)

# XYZ Coordinates
tk.Label(root,text="(Location)",font=("Arial",9,"bold")).place(x=10,y=80)

x_lbl = tk.Label(root,text="x: ")
x_lbl.place(x=85,y=80)
x_entry = tk.Entry(root,width=4)
x_entry.place(x=105,y=81)

y_lbl = tk.Label(root,text="y: ")
y_lbl.place(x=145,y=80)
y_entry = tk.Entry(root,width=4)
y_entry.place(x=165,y=81)

z_lbl = tk.Label(root,text="z: ")
z_lbl.place(x=205,y=80)
z_entry = tk.Entry(root,width=4)
z_entry.place(x=225,y=81)

# Shape Dimensions
def dimensions(*args):
    selected_shape = shape_prompt.get()

    if selected_shape == "Square-based Pyramid":
        dimension_1.set("Base Length:")
        dimension_2.set("Height:")
        dimension_entry_1.place(x=90,y=120)
        dimension_entry_2.place(x=90,y=150)

    elif selected_shape == "Icosahedron":
        dimension_1.set("Side Length:")
        dimension_2.set("")
        dimension_entry_1.place(x=90,y=120)
        dimension_entry_2.place_forget()

    else:
        dimension_1.set("Please choose a 3D shape type!")
        dimension_2.set("")

dimension_1 = tk.StringVar()
dimension_lbl_1 = tk.Label(root,textvariable=dimension_1)
dimension_lbl_1.place(x=10, y=120)
dimension_entry_1 = tk.Entry(root,width=25)
dimension_entry_1.place_forget()

dimension_2 = tk.StringVar()
dimension_lbl_2 = tk.Label(root,textvariable=dimension_2)
dimension_lbl_2.place(x=10, y=150)
dimension_entry_2 = tk.Entry(root,width=25)
dimension_entry_2.place_forget()

shape_prompt.trace_add("write",dimensions)

# Shape Creation
def check_values():
    try:
        r = int(red_entry.get().strip())
        g = int(green_entry.get().strip())
        b = int(blue_entry.get().strip())
        if r > 255 or r < 0 or g > 255 or g < 0 or b > 255 or b < 0:
            output.set("Please check the RGB values!")
        else:
            rgb = [r,g,b]
            try:
                x = int(x_entry.get().strip())
                y = int(y_entry.get().strip())
                z = int(z_entry.get().strip())
                if not x or not y or not z:
                    output.set("Please check the location values!")
                else:
                    coord = [x,y,z]
                    selected_shape = shape_prompt.get()
                    if selected_shape == "Square-based Pyramid":
                        pyramid(rgb,coord)
                    elif selected_shape == "Icosahedron":
                        icosahedron(rgb,coord)
                    else:
                        output.set("Please choose a 3D shape type!")
            except ValueError:
                output.set("Please check the location values!")
    except ValueError:
        output.set("Please check the RGB values!")

def pyramid(rgb,coord):
    try:
        b = int(dimension_entry_1.get().strip())
        h = int(dimension_entry_2.get().strip())
        if not b or not h:
            output.set("Please check the dimensions!")
        else:
            pyr = SquarePyramid(rgb, coord, b, h)
            output.set(f"{pyr.getType()}\nVolume: {pyr.volume():.2f} units cubed\nSurface Area: {pyr.surface_area():.2f} units squared")
            output_lbl.place(x=53,y=235)
            pyr.draw()
    except ValueError:
        output.set("Please check the dimensions!")

def icosahedron(rgb, coord):
    try:
        s = int(dimension_entry_1.get().strip())
        if not s:
            output.set("Please check the dimensions!")
        else:
            ico = Icosahedron(rgb, coord, s)
            output.set(f"{ico.getType()}\nVolume: {ico.volume():.2f} units cubed\nSurface Area: {ico.surface_area():.2f} units squared")
            output_lbl.place(x=53,y=235)
            ico.draw()
    except ValueError:
        output.set("Please check the dimensions!")


output = tk.StringVar()
output_lbl = tk.Label(root,textvariable=output)
output_lbl.place(x=61,y=250)
output.set("")

tk.Button(root,text="Create Shape",command=check_values).place(x=100,y=200)

root.mainloop()