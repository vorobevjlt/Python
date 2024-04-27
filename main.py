from tkinter import *
import random
import time
def left(event):
    x =- 10
    y = 0
    canvas.move(present_unit, x, y)

def right(event):
    x =+ 10
    y = 0
    canvas.move(present_unit, x, y)

def up(event):
    x = 0
    y =- 10
    canvas.move(present_unit, x, y)

def down(event):
    x = 0
    y =+ 10
    canvas.move(present_unit, x, y)

def move_forw():
    x = 0
    y =+ 10
    canvas.move(present_unit, x, y)

WIDTH = 400
HEIGHT = 600
BACKGROUND_COLOR = "#31554f"
x = 0
y = 0

root = Tk()

root.geometry("400x600")
 
canvas = Canvas(root, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)

present_unit = canvas.create_rectangle(x, y, x + 20, y + 20, fill="#80CBC4")

canvas.pack()

def move_start():
    x =+ 1
    y =+ 1
    canvas.move(present_unit, y, x)    
    root.after(50, move_start)

def move_stop():
    root.after_cancel(move_stop)

# canvas.bind_all('<KeyPress-Down>', move_start)
# canvas.bind_all('<KeyRelease-Down>', move_stop)

# root.bind('<Left>', left)

# root.bind('<Right>', right)

# root.bind('<Up>', up)

# root.bind('<Down>', down)

move_start()

if __name__ == "__main__":
    root.mainloop()