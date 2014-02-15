# CS 408 - Programming Lanuages
# Connect 5 game

import tkinter
from tkinter        import messagebox
from RulesFactory   import RulesFactory
from Board          import Board

#Initialize tkinter
root = tkinter.Tk()

#Set pixel width/height of cell
cell_width = 50

#Number of rows/columns
num_rows = 12

#Size of the canvas we're rendering on
canvas_size = num_rows * cell_width

#Current move's player color
current_player = 'w' #w is for white

#Board to use with 10 rows/columns (square board)
board = Board(10)

#Rules to use
rules = RulesFactory(board)

def mAlert(aTitle, bMessage):
    messagebox.showinfo(title=aTitle, message=bMessage)

"""
    When the game board is clicked, draw the piece on the board and alternate
    player turns.
"""
def drawPiece(event):
    global current_player
    cellX = int(event.x / cell_width)
    cellY = int(event.y / cell_width)
    
    print(cellX, cellY)
    
    cellXTopLeft = cell_width * cellX
    cellYTopLeft = cell_width * cellY
    if current_player == 'w':
        if rules.isLegalFor( 'w', cellX, cellY ):
            board.addPieceAt( 'w', cellX, cellY )
            w.create_oval(cellXTopLeft, cellYTopLeft, cellXTopLeft + cell_width, cellYTopLeft + cell_width, fill="white")
            current_player = 'b'
            mAlert("farts", "a lot")
        else:
            #Not a valid move, do nothing
            pass
    else:
        if rules.isLegalFor( 'b', cellX, cellY ):
            board.addPieceAt( 'b', cellX, cellY )
            w.create_oval( cellXTopLeft, cellYTopLeft, cellXTopLeft + cell_width, cellYTopLeft + cell_width, fill="black")
            current_player = 'w'
        else:
            #Not a valid move, do nothing
            pass

w = tkinter.Canvas(root, width = canvas_size, height = canvas_size)
w.bind("<Button-1>", drawPiece)

for x in range(canvas_size):
    if x % cell_width == 0:
        w.create_line(x, 0, x, canvas_size)
        w.create_line(0, x, canvas_size, x)
    
w.pack()
root.mainloop()
