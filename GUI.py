from tkinter import *

root = Tk()
canvas_size = 950
cell_width = 50


def draw(event):
    cellX = cell_width*int(event.x/cell_width)
    cellY = cell_width*int(event.y/cell_width)
    w.create_oval( cellX, cellY, cellX+cell_width, cellY+cell_width, fill = "red")


w = Canvas(root, width=canvas_size, height=canvas_size)
w.bind("<Button-1>", draw)

for x in range(canvas_size):
    if x%cell_width == 0:
        w.create_line( x, 0, x, canvas_size )
        w.create_line( 0, x, canvas_size, x )

w.pack()
root.mainloop()
