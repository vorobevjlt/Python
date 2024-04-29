from tkinter import *
import random
import time
cell = [405]
speed = 10
class Position:
    def __init__(self, x = 0, y = 0):
        self.x = random.choice(cell)
        self.y = y

#game window
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg = "black", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, borderwidth = 0, highlightthickness = 0)
canvas.pack()

def move_start():
    unit.y = unit.y + 1
    canvas.delete("s_unit")
    if unit.x + unit_shape.shape_x > WIDTH:
        unit.x = 400
        lay_ground = unit.x - unit_shape.shape_x

        position = canvas.create_rectangle(
            unit.x, unit.y, 
            lay_ground, 
            unit.y - unit_shape.shape_y, 
            fill="#80CBC4",
            tags="s_unit"
            )
        
    elif unit.x + unit_shape.shape_x < WIDTH:
        unit.x = 5
        lay_ground = unit.x + unit_shape.shape_x

        position = canvas.create_rectangle(
            unit.x, unit.y, 
            lay_ground, 
            unit.y - unit_shape.shape_y, 
            fill="#80CBC4",
            tags="s_unit"
            )        
    else:
        lay_ground = unit.x - unit_shape.shape_x

        position = canvas.create_rectangle(
            unit.x, unit.y, 
            lay_ground,
            unit.y - unit_shape.shape_y, 
            fill="#80CBC4",
            tags="s_unit"
            )
        
    repeat = root.after(speed, move_start)

    if unit.y >= 200 or (unit.y - unit_shape.shape_y) >= 200:

        position = canvas.create_rectangle(
            unit.x, unit.y, 
            lay_ground, 
            unit.y - unit_shape.shape_y,
            fill="#80CBC4",
            tags="stay_unit"
            )
        print((unit.x + unit_shape.shape_x), (unit.y - unit_shape.shape_y))
        root.after_cancel(repeat)
        unit.y = 0
        unit.x = random.choice(cell)
        move_start()       

move_start()

def up(event):
    if unit_shape.shape_x == 20:
        unit_shape.shape_x = 80
        unit_shape.shape_y = 20
    else:
        unit_shape.shape_x = 20
        unit_shape.shape_y = 80

def left(event):
    idx = cell.index(unit.x)
    unit.x = cell[idx - 1]

def right(event):
    unit.x - 20

# def right(event):
#     x =+ 10
#     y = 0
#     canvas.move(present_unit, x, y)

# def left(event):
#     x = 0
#     y =- 10
#     canvas.move(present_unit, x, y)

# def down(event):
#     x = 0
#     y =+ 10
#     canvas.move(present_unit, x, y)

# def move_forw():
#     x = 0
#     y =+ 10
#     canvas.move(present_unit, x, y)

root.bind('<Up>', up)

root.bind('<Right>', right)

root.bind('<Left>', left)

# root.bind('<Down>', down)

if __name__ == "__main__":
    root.mainloop()
    