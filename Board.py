from Piece import Piece

""" Manages the pieces and the moves made on the board """
class Board(object):
    
    """ Initialize board with width and height of specified size """
    def __init__(self, size):
        self.size = size
        self.board = [['-' for i in range(size)] for j in range(size)]
        
    """ Add a piece of the specified row and column. """
    def addPieceAt(self, piece, row, col):
        if self.pointIsOutOfBounds(row, col):
            return
        
        self.board[row][col] = piece.color

    """ Get the piece at specified row and column """
    def getPieceAt(self, row, col):
        if self.pointIsOutOfBounds(row, col):
            return None

        return self.board[row][col]

    """ Checks if move is valid for given piece """
    def isLegalFor(self, piece, row, col):
        if self.pointIsOutOfBounds(row, col):
            return False
        
        return self.board[row][col] == '-'

    """ Determines if the row or column is out of the boundaries of the board """
    def pointIsOutOfBounds(self, row, col):
        return row < 0 or row >= self.size or col < 0 or col >= self.size

    """ Check for vertical, horizontal, and diagonal victories. """
    def checkForVictoryWithPoint(self, row, col):
        if self.pointIsOutOfBounds(row, col):
            return False

        color = self.board[row][col]

        if color == '-':
            return False
        
        if self.checkVertical(col, color) or self.checkHorizontal(row, color) or self.checkDiagonalPositiveSlope(row, col, color) or self.checkDiagonalNegativeSlope(row, col, color):
            return True
        else:
            return False

    """ Check if there are 5 pieces of the same color in the given column """
    def checkVertical(self, col, color):
        count = 0
        for row in range(self.size):
            if self.board[row][col] == color:
                count += 1
                if count == 5:
                    return True
            else:
                count = 0
        return False
            
    """ Check if there are 5 pieces of the same color in the given row """
    def checkHorizontal(self, row, color):
        count = 0
        for col in range(self.size):
            if self.board[row][col] == color:
                count += 1
                if count == 5:
                    return True
            else:
                count = 0
        return False

    """ Check diagonal with positive slope for 5 pieces of the same color in a row """
    def checkDiagonalPositiveSlope(self, row, col, color):
        rowColDictionary = self.findTopRight(row, col)
        startingRow = rowColDictionary["row"]
        startingCol = rowColDictionary["col"]
        count = 0
        for col in range(startingCol, -1, -1):
            if startingRow >= self.size:
                return False
            
            if self.board[startingRow][col] == color:
                count += 1
                if count == 5:
                    return True
            else:
                count = 0
                
            startingRow += 1
        return False

    """ Find the top-right point of a diagonal with a positive slope based on given point.
        Returns a dictionary with "row" and "col" as the keys to access the row and column
        values respectively. """
    def findTopRight(self, row, col):
        # Find width between given point and the end of the board
        deltaX = self.size - col - 1

        # Get the starting row by moving up by deltaX amount of spaces from the given point's y-coordinate
        # (You can think of it as making an isosceles right triangle by moving to the right and then up
        # an equal amount of spaces)
        startingRow = row - deltaX

        # If the starting row is less than 0, then we have to make the isosceles right triangle by going
        # up and then right in the same manner as described earlier.
        if startingRow < 0:
            return {"row":0, "col":col + row}
        else:
            return {"row":startingRow, "col":self.size - 1}

    """ Check diagonal with negative slope for 5 pieces of the same color in a row """
    def checkDiagonalNegativeSlope(self, row, col, color):
        rowColDictionary = self.findTopLeft(row, col)
        startingRow = rowColDictionary["row"]
        startingCol = rowColDictionary["col"]
        count = 0
        for col in range(startingCol, self.size):
            if startingRow >= self.size:
                return False
            
            if self.board[startingRow][col] == color:
                count += 1
                if count == 5:
                    return True
            else:
                count = 0

            startingRow += 1
        return False

    """ Find the top-left poing of a diagonal with a negative slope based on given point.
        Returns a dictionary with "row" and "col" as the keys to access the row and column
        values respectively. """
    def findTopLeft(self, row, col):
        # Find the starting row by subtracting from the existing row by the column (here, the column is
        # essential the width from the starting edge of the board to the said column.  You can also
        # think of this as making an isosceles right triangle by moving left to the edge of the board,
        # and then moving up an equal amount of spaces).
        startingRow = row - col

        # If the starting row is less than 0, then we have to make the isosceles right triangle by going
        # up and then left in the same manner as described earlier.
        if startingRow < 0:
            return {"row":0, "col":col - row}
        else:
            return {"row":startingRow, "col":0}
        

    """Print contents of board"""
    def printBoard(self):
        for row in self.board:
            print(" ".join(row))
        print()

""" TEST CODE """

"""
board = Board(11)
board.addPieceAt(Piece('b'), 2, 3)
board.addPieceAt(Piece('b'), 3, 4)
board.addPieceAt(Piece('b'), 4, 5)
board.addPieceAt(Piece('b'), 5, 6)
board.addPieceAt(Piece('b'), 6, 7)
board.printBoard()

if board.checkForVictoryWithPoint(3, 4):
    print("Black is the victor")
else:
    print("Don't know who wins yet")

board.addPieceAt(Piece('w'), 8, 4)
board.addPieceAt(Piece('w'), 8, 5)
board.addPieceAt(Piece('w'), 8, 6)
board.addPieceAt(Piece('w'), 8, 7)
#board.addPieceAt(Piece('w'), 8, 8)
board.printBoard()

if board.checkForVictoryWithPoint(8, 7):
    print("White is the victor")
else:
    print("Winner is undetermined")

board.addPieceAt(Piece('b'), 1, 2)
board.addPieceAt(Piece('b'), 2, 2)
board.addPieceAt(Piece('b'), 3, 2)
board.addPieceAt(Piece('b'), 4, 2)
#board.addPieceAt(Piece('b'), 5, 2)
board.printBoard()

if board.checkForVictoryWithPoint(1, 2):
    print("Black is the victor")
else:
    print("Winner is undetermined")

print("--------")

rowColDictionary = board.findTopLeft(10, 0)
print(rowColDictionary["row"])
print(rowColDictionary["col"])

print("--------")

board.addPieceAt(Piece('w'), 10, 0)
board.addPieceAt(Piece('w'), 9, 1)
board.addPieceAt(Piece('w'), 8, 2)
board.addPieceAt(Piece('w'), 7, 3)
#board.addPieceAt(Piece('w'), 6, 4)
board.printBoard()

if board.checkForVictoryWithPoint(10, 0):
    print("White is the victor with a diagonal going up and to the right")
else:
    print("Winner undetermined")

"""
