# CS 408 - Programming Lanuages
# Connect 5 game

import tkinter
import RulesFactory

#Initialize tkinter
root = tkinter.Tk()

#Set pixel width/height of cell
cell_width = 50

#Size of the canvas we're rendering on
canvas_size = 550

#Current move's player color
current_player = 'w' #w is for white

"""
    When the game board is clicked, draw the piece on the board and alternate
    player turns.
"""
def drawPiece(event):
    global current_player
    cellX = int(event.x / cell_width)
    cellY = int(event.y / cell_width)
    cellXTopLeft = cell_width * cellX
    cellYTopLeft = cell_width * cellY
    if current_player == 'w':
        w.create_oval(cellXTopLeft, cellYTopLeft, cellXTopLeft + cell_width, cellYTopLeft + cell_width, fill="white")
        current_player = 'b'
    else:
        w.create_oval( cellXTopLeft, cellYTopLeft, cellXTopLeft + cell_width, cellYTopLeft + cell_width, fill="black")
        current_player = 'w'

w = tkinter.Canvas(root, width = canvas_size, height = canvas_size)
w.bind("<Button-1>", drawPiece)

for x in range(canvas_size):
    if x % cell_width == 0:
        w.create_line(x, 0, x, canvas_size)
        w.create_line(0, x, canvas_size, x)
    
w.pack()
root.mainloop()
