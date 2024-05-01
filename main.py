from tkinter import *
import random
from bisect import bisect
# Клетки по оси Х
x_cell = [25, 45, 65, 85, 105, 125, 145, 165, 185, 205]
# Клетки по оси Y
y_cell = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640]
apearCell = [165,185,205]
speed = 10

class Form:
    def __init__(self, shape_x = 0, shape_y = 0):
        self.shape_x = 20
        self.shape_y = 80

class Ground:
    def __init__(self, shape_x = 0):
        self.height = 0

w = 225
h = 600
b = "#31554f"
unit_shape = Form()
field_ground = Ground()
shape_x = 0
shape_y = 0
root = Tk()
root.geometry("400x600")
canvas = Canvas(root, bg=b, height=h, width=w)
canvas.pack()


class Position:
    def __init__(self, x = 0, y = 0):
        self.x = random.choice(apearCell)
        self.y = y
        # Игровое поле ввиде матрицы значений (True, False)
        # Каждый ключ это одно из значений y_cell
        self.field = {20: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 40: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 60: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 80: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 100: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 120: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 140: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 160: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 180: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 200: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 220: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 240: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 260: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 280: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 300: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 320: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 340: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 360: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 380: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 400: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 420: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 440: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 460: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 480: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 500: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 520: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 540: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 560: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 580: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 600: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}, 620: {25: True, 45: True, 65: True, 85: True, 105: True, 125: True, 145: True, 165: True, 185: True, 205: True}, 640: {25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False}}

    def get_condition(self, x, y):
        return self.field[y][x]

    def get_y_pos(self, y):
        idx = bisect(y_cell, y)
        return y_cell[idx]

    
    def change_condition(self, begin_x, end_x, begin_y, end_y):
        x_coor = []
        y_coor = []
        for i in range(begin_x, end_x, 20):
            x_coor.append(i)
        for j in range(begin_y, end_y, -20):
            y_coor.append(j)
        for y in y_coor:
            for x in x_coor:
                self.field[y][x] = True
      
unit = Position()

def move_start():
    unit.y = unit.y + 1
    canvas.delete("s_unit")
    shape_x = unit.x + unit_shape.shape_x
    shape_y = unit.y - unit_shape.shape_y
    position = canvas.create_rectangle(
            unit.x, unit.y, 
            shape_x,
            shape_y, 
            fill="#80CBC4",
            tags="s_unit"
            )
    repeat = root.after(speed, move_start)
    idx = bisect(y_cell, unit.y)
    if unit.get_condition(unit.x, y_cell[idx]):
        position = canvas.create_rectangle(
            unit.x, unit.y, 
            shape_x,
            shape_y, 
            fill="#80CBC4",
            tags="stay_unit"
            )
        unit.change_condition(unit.x, shape_x, unit.y, shape_y)
        for k, v in unit.field.items():
            print(k, v)        
        root.after_cancel(repeat)
        unit.y = 0
        unit.x = random.choice(apearCell)
        move_start()          

def up(event):
    pass

def left(event):
    pass

def right(event):
    y = unit.get_y_pos(unit.y)
    x = unit.x + 20
    if x in x_cell:
        unit.x = unit.x + 20
        print(unit.get_condition(x, y))

def speedUp(event):
    for k, v in unit.field.items():
        if k >= y_cell[bisect(y_cell, unit.y)] and v[unit.x]:
            unit.y = k - 21
            break

root.bind('<Up>', up)

root.bind('<Right>', right)

root.bind('<Left>', left)

root.bind('<Down>', speedUp)

move_start()

if __name__ == "__main__":
    root.mainloop()