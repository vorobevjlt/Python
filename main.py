from tkinter import *
import random
cell = [25, 45, 65, 85, 105, 125, 145, 165, 185, 205]
apearCell = [85, 105, 125]
speed = 10
class Position:
    def __init__(self, x = 0, y = 0):
        self.x = random.choice(apearCell)
        self.y = y
        self.cell = {25:600, 45:600, 65:600, 85:600, 105:600, 125:600, 145:600, 165:600, 185:600, 205:600}

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
unit = Position()
unit_shape = Form()
field_ground = Ground()
lay_ground = 0
save_right = 0
root = Tk()
root.geometry("400x600")
canvas = Canvas(root, bg=b, height=h, width=w)
canvas.pack()

def move_start():
    unit.y = unit.y + 1
    canvas.delete("s_unit")
    lay_ground = unit.x + unit_shape.shape_x
    matchedKeys = [unit.cell[k] for k in unit.cell.keys() if k >= unit.x and k < (unit.x + unit_shape.shape_x)]
    field_ground.height = min(matchedKeys)
    print(field_ground.height)
    position = canvas.create_rectangle(
            unit.x, unit.y, 
            lay_ground,
            unit.y - unit_shape.shape_y, 
            fill="#80CBC4",
            tags="s_unit"
            )
        
    repeat = root.after(speed, move_start)

    if unit.y >= field_ground.height or (unit.y - unit_shape.shape_y) >= field_ground.height:
        position = canvas.create_rectangle(
            unit.x, unit.y, 
            lay_ground, 
            unit.y - unit_shape.shape_y,
            fill="#80CBC4",
            tags="stay_unit"
            )
        
        root.after_cancel(repeat)
        cellValues = []
        matchedKeys = [k for k in unit.cell.keys() if k >= unit.x and k < (unit.x + unit_shape.shape_x)]
        for i in matchedKeys:
            unit.cell[i] = unit.cell[i] - unit_shape.shape_y
            cellValues.append(unit.cell[i])
        for i in matchedKeys:
            unit.cell[i] = min(cellValues)
        unit.y = 0
        unit.x = random.choice(apearCell)
        move_start()       

def up(event):
    if unit.x > cell[-5] and unit_shape.shape_y == 80:
        unit.x = cell[-5]
        unit_shape.shape_x = 80
        unit_shape.shape_y = 20
    elif unit.x <= cell[-5] and unit_shape.shape_y == 80:
        unit_shape.shape_x = 80
        unit_shape.shape_y = 20
    else:
        unit_shape.shape_x = 20
        unit_shape.shape_y = 80

def left(event):
    idx = cell.index(unit.x)
    if idx == 0:
        unit.x = cell[idx]
    else:    
        unit.x = cell[idx - 1]

def right(event):
    idx = cell.index(unit.x) 
    if idx == len(cell)-2:
        unit.x = cell[idx]
    elif (unit.x + unit_shape.shape_x > cell[-1]) and (unit_shape.shape_y == 80):
        unit.x = cell[-2]
    elif (unit.x + unit_shape.shape_x > cell[-2]) and (unit_shape.shape_y == 20):
        unit.x = cell[-5]        
    else:    
        unit.x = cell[idx + 1]

def speedUp(event):
    unit.y = field_ground.height - 1

move_start()

root.bind('<Up>', up)

root.bind('<Right>', right)

root.bind('<Left>', left)

root.bind('<Down>', speedUp)

if __name__ == "__main__":
    root.mainloop()