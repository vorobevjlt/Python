from tkinter import *
import random
from bisect import bisect
from config import *
# Клетки по оси Х
x_cell = [-15, 5, 25, 45, 65, 85, 105, 125, 145, 165, 185, 205, 225]
# Клетки по оси Y
y_cell = [-80 ,-60, -40 ,-20, 0 ,20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640]
apearCell = [105,125]
speed = 10

class Form:
    def __init__(self, shape_x = 0, shape_y = 0):
        self.shape_x = 20
        self.shape_y = 80

unit_shape = Form()

class Position:
    def __init__(self, x = 0, y = 0):
        self.x = random.choice(apearCell)
        self.y = y
        self.flag_left = 0
        self.flag_right = 0
        # Игровое поле ввиде матрицы значений (True, False)
        # Каждый ключ это одно из значений y_cell
        self.field = {20: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 40: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 60: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 80: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 100: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 120: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 140: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 160: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 180: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 200: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 220: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 240: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 260: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 280: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 300: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 320: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 340: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 360: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 380: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 400: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 420: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 440: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 460: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 480: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 500: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 520: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 540: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 560: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 580: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 600: {-15: True, 5: False, 25: False, 45: False, 65: False, 85: False, 105: False, 125: False, 145: False, 165: False, 185: False, 205: False, 225: True}, 620: {-15: True, 5: True, 25: True, 45: True, 65: True, 85: True, 105: True, 125: True, 145: True, 165: True, 185: True, 205: True, 225: True}, 640: {-15: True, 5: True, 25: True, 45: True, 65: True, 85: True, 105: True, 125: True, 145: True, 165: True, 185: True, 205: True, 225: True}}


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

    def edge(self):

        y = self.get_y_pos(self.y)
        if self.x == x_cell[0]:
            x_right = x_cell[-1]
        elif self.x - unit_shape.shape_x < x_cell[0]:
            x_left = x_cell[0]
        else:
            x_right = self.x + unit_shape.shape_x
            x_left = self.x - unit_shape.shape_x
        if self.get_condition(x_left, y) and self.get_condition(x_right, y):
            self.flag_left = self.y + shape_y
            self.flag_right = self.y + shape_y
        elif self.get_condition(x_left, y):
            self.flag_left = self.y + shape_y
        elif self.get_condition(x_right, y):
            self.flag_right = self.y + shape_y
        else:
            self.flag_left = 0
            self.flag_right = 0
      
unit = Position()

def move_start():
    unit.y += 1
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
    unit.edge()
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
    if unit.y > unit.flag_left and (unit.x - 20) >= x_cell[0]:
        unit.x -= 20

def right(event):
    if unit.y > unit.flag_right and (unit.x + 20) <= x_cell[-1]:
        unit.x += 20

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