from shapes import SquarePyramid, Icosahedron
import tkinter as tk

pyramid = SquarePyramid([1,1,1], [0,0,0], 1, 1)
ico = Icosahedron([1,1,1], [0,0,0], 1)

def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb

# --- Input Window --- #
root = tk.Tk()
root.title("3D Shapes App")
root.geometry("340x280")
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
def dimensions():
    selected_shape = shape_prompt.get()

    if selected_shape == "Square-based Pyramid":
        dimension_1.set("Base Length:")
        dimension_2.set("Height:")
        dimension_entry_1.place(x=220,y=133)
        dimension_entry_2.place(x=220,y=163)

    elif selected_shape == "Icosahedron":
        dimension_1.set("Side Length:")
        dimension_2.set("")
        dimension_entry_1.place(x=220,y=133)
        dimension_entry_2.place_forget()

    else:
        dimension_1.set("Please choose a shape!")
        dimension_2.set("")

dimension_1 = tk.StringVar()
dimension_lbl_1 = tk.Label(root,textvariable=dimension_1)
dimension_lbl_1.place(x=140, y=133)
dimension_entry_1 = tk.Entry(root,width=10)
dimension_entry_1.place_forget()

dimension_2 = tk.StringVar()
dimension_lbl_2 = tk.Label(root,textvariable=dimension_2)
dimension_lbl_2.place(x=140, y=163)
dimension_entry_2 = tk.Entry(root,width=10)
dimension_entry_2.place_forget()

tk.Button(root,text="Refresh Dimensions",command=dimensions).place(x=10,y=130)

# Instantiation & Visualization
def check_values():
    pass

def instantiate():
    pass

def visualize():
    selected_shape = shape_prompt.get()

    if selected_shape == "Square-based Pyramid":
        pyramid.draw()
        output.set("")

    elif selected_shape == "Icosahedron":
        ico.draw()
        output.set("")

    else:
        output.set("Please choose a shape!")

output = tk.StringVar()
output_lbl = tk.Label(root,textvariable=output)
output_lbl.place(x=10,y=235)
output.set("")

tk.Button(root,text="Create a Shape",command=instantiate).place(x=10,y=200)
tk.Button(root,text="Visualize",command=visualize).place(x=110,y=200)

root.mainloop()