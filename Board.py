from Piece import Piece

"""Manages the pieces and moves made on the board"""
class Board(object):
    """Initialize board with width and height of specified size"""
    def __init__(self, size):
        self.size = size
        self.board = [['-' for i in range(size)] for j in range(size)]
        
    """Add a piece of the specified row and column."""
    def addPieceAt(self, piece, row, col):
        if self.pointIsOutOfBounds(row, col):
            return
        
        self.board[row][col] = piece.color

    """Get the piece at specified row and column"""
    def getPieceAt(self, row, col):
        if self.pointIsOutOfBounds(row, col):
            return None

        return self.board[row][col]

    """Checks if move is valid for given piece"""
    def isLegalFor(self, piece, row, col):
        if self.pointIsOutOfBounds(row, col):
            return False
        
        return self.board[row][col] == '-'

    def pointIsOutOfBounds(self, row, col):
        return row < 0 or row >= self.size or col < 0 or col >= self.size

    """Check for vertical, horizontal, and diagonal victories."""
    def checkForVictoryWithPoint(self, row, col):
        if self.pointIsOutOfBounds(row, col):
            return False

        color = self.board[row][col]
        if self.checkVertical(col, color) or self.checkHorizontal(row, color) or self.checkDiagonalPositiveSlope(row, col, color) or self.checkDiagonalNegativeSlope(row, col, color):
            return True
        else:
            return False

    """Check if there are 5 pieces of the same color in the given column"""
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
            
    """Check if there are 5 pieces of the same color in the given row"""
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

    """Check diagonal with positive slope"""
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

    """Find the top-right point of a diagonal with a positive slope based on given point.
       Returns a dictionary.  Use "row" and "col" as the keys to access the row and col values respectively."""
    def findTopRight(self, row, col):
        deltaX = self.size - col - 1
        startingRow = row - deltaX
        if startingRow < 0:
            return {"row":0, "col":col + row}
        else:
            return {"row":startingRow, "col":self.size - 1}

    def checkDiagonalNegativeSlope(self, row, col, color):
        rowColDictionary = self.findTopLeft(row, col)
        startingRow = rowColDictionary["row"]
        startingCol = rowColDictionary["col"]
        count = 0
        for col in range(self.size):
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

    def findTopLeft(self, row, col):
        startingRow = row - col
        if startingRow < 0:
            return {"row":0, "col":col - row}
        else:
            return {"row":startingRow, "col":0}
        

    """Print contents of board"""
    def printBoard(self):
        for row in self.board:
            print(" ".join(row))
        print()

board = Board(11)
board.addPieceAt(Piece('b'), 2, 3)
board.addPieceAt(Piece('b'), 3, 4)
board.addPieceAt(Piece('b'), 4, 5)
board.addPieceAt(Piece('b'), 5, 6)
board.addPieceAt(Piece('b'), 6, 7)
board.printBoard()

if board.checkForVictoryWithPoint(3, 4):
    print("Black is the victory")
else:
    print("Don't know who wins yet")
