from tkinter import *

root = Tk()
boardN_N = 19
cell_width = 50
canvas_size = cell_width*boardN_N
player = "red"
logicBoard = [["-" for x in range(boardN_N)] for x in range(boardN_N)] 

def alternatePlayer():
    global player
    if player == "red":
        player = "black"
        return "red"
    else:
        player = "red"
        return "black"

def place(event):
    global logicBoard
    global player
    cellX = int(event.x/cell_width)
    cellY = int(event.y/cell_width)
    if logicBoard[cellX][cellY] == "-": #no else needed
        logicBoard[cellX][cellY] = player
        #run connect 5 logic on this line?
        cellXTopLeft = cell_width*cellX
        cellYTopLeft = cell_width*cellY
        w.create_oval( cellXTopLeft, cellYTopLeft, cellXTopLeft+cell_width, cellYTopLeft+cell_width, fill = alternatePlayer())
        
        

w = Canvas(root, width=canvas_size, height=canvas_size)
w.bind("<Button-1>", place)

for x in range(canvas_size):
    if x%cell_width == 0:
        w.create_line( x, 0, x, canvas_size )
        w.create_line( 0, x, canvas_size, x )

w.pack()
root.mainloop()

