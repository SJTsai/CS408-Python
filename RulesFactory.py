from Board import Board
from Piece import Piece

""" Implementation of Connect 5 rules """
class RulesFactory(object):
    """
    def __init__(self, size):
        self.size = size

    Return True if the color wins, False otherwise.

    def checkWin(color, xPos, yPos):
        #The counter for the number we've found in a row
        in_a_row = 1
        
        #Check up-down (up first)
        for y in range(yPos + 1, size):
            if Board.getPieceAt(xPos, y).getColor() == color:
                if in_a_row == 5:
                    return True
                else:
                    in_a_row += 1
            else:
                break
        if in_a_row != 5:
            #Time to check down
            counter = size - yPos
            if counter < 5 - in_a_row:
                break
            
            #Count from the slot below the yPos to index 0
            for y in range(yPos - 1, -1, -1):
                if Board.getPieceAt(xPos, y).getColor() == color:
                    if in_a_row == 5:
                        return True
                    else:
                        in_a_row += 1
                else:
                    break
    """
    
    """ Checks if move is valid for given piece """
    def isLegalFor(self, piece, row, col, board):
        if self.pointIsOutOfBounds(row, col, board):
            return False
        
        return board.getBoard()[row][col] is None

    """ Checks if the Piece (if it exists) at the specified point
        is the same color as the one provided """
    def isPieceAtPointEqualToColor(self, row, col, color, board):
        if self.pointIsOutOfBounds(row, col, board):
            return False
        
        piece = board.getBoard()[row][col]
        if not piece is None:
            if piece.color == color:
                return True
            return False
        return False

    """ Determines if the row or column is out of the boundaries of the board """
    def pointIsOutOfBounds(self, row, col, board):
        return row < 0 or row >= board.getSize() or col < 0 or col >= board.getSize()

    """ Check for vertical, horizontal, and diagonal victories. """
    def checkForVictoryWithPoint(self, row, col, board):
        if self.pointIsOutOfBounds(row, col, board):
            return False

        piece = board.getBoard()[row][col]
        if not piece is None:
            color = piece.color
        else:
            return False

        if color == '-':
            return False
        
        if self.checkVertical(col, color, board) or self.checkHorizontal(row, color, board) or self.checkDiagonalPositiveSlope(row, col, color, board) or self.checkDiagonalNegativeSlope(row, col, color, board):
            return True
        else:
            return False

    """ Check if there are 5 pieces of the same color in the given column """
    def checkVertical(self, col, color, board):
        count = 0
        for row in range(board.getSize()):
            if self.isPieceAtPointEqualToColor(row, col, color, board):
                count += 1
                if count == 5:
                    return True
            else:
                count = 0
        return False
            
    """ Check if there are 5 pieces of the same color in the given row """
    def checkHorizontal(self, row, color, board):
        count = 0
        for col in range(board.getSize()):
            if self.isPieceAtPointEqualToColor(row, col, color, board):
                count += 1
                if count == 5:
                    return True
            else:
                count = 0
        return False

    """ Check diagonal with positive slope for 5 pieces of the same color in a row """
    def checkDiagonalPositiveSlope(self, row, col, color, board):
        rowColDictionary = self.findTopRight(row, col, board)
        startingRow = rowColDictionary["row"]
        startingCol = rowColDictionary["col"]
        count = 0
        boardSize = board.getSize()
        for col in range(startingCol, -1, -1):
            if startingRow >= boardSize:
                return False

            if self.isPieceAtPointEqualToColor(startingRow, col, color, board):
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
    def findTopRight(self, row, col, board):
        boardSize = board.getSize()
        
        # Find width between given point and the end of the board
        deltaX = boardSize - col - 1

        # Get the starting row by moving up by deltaX amount of spaces from the given point's y-coordinate
        # (You can think of it as making an isosceles right triangle by moving to the right to the edge of
        # the board, and then moving up an equal amount of spaces)
        startingRow = row - deltaX

        # If the starting row is less than 0, then we have to make the isosceles right triangle by going
        # up and then right in the same manner as described earlier.
        if startingRow < 0:
            return {"row":0, "col":col + row}
        else:
            return {"row":startingRow, "col":boardSize - 1}

    """ Check diagonal with negative slope for 5 pieces of the same color in a row """
    def checkDiagonalNegativeSlope(self, row, col, color, board):
        rowColDictionary = self.findTopLeft(row, col, board)
        startingRow = rowColDictionary["row"]
        startingCol = rowColDictionary["col"]
        count = 0
        boardSize = board.getSize()
        for col in range(startingCol, boardSize):
            if startingRow >= boardSize:
                return False
            if self.isPieceAtPointEqualToColor(startingRow, col, color, board):
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
    def findTopLeft(self, row, col, board):
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

# TEST CODE

"""
board = Board(11)

print("CHECK VERTICAL")
#board.addPieceAt(Piece('w'), 2, 3)
board.addPieceAt(Piece('w'), 3, 3)
board.addPieceAt(Piece('w'), 4, 3)
board.addPieceAt(Piece('w'), 5, 3)
board.addPieceAt(Piece('w'), 6, 3)
#board.printBoard()
rules = RulesFactory()
if rules.checkForVictoryWithPoint(2, 3, board):
    print("White wins!")
else:
    print("Winner undetermined.")

print()
print("CHECK HORIZONTAL")
#board.addPieceAt(Piece('b'), 4, 4)
board.addPieceAt(Piece('b'), 4, 5)
board.addPieceAt(Piece('b'), 4, 6)
board.addPieceAt(Piece('b'), 4, 7)
board.addPieceAt(Piece('b'), 4, 8)
#board.printBoard()
if rules.checkForVictoryWithPoint(4, 4, board):
    print("Black wins!")
else:
    print("Winner undetermined.")

print()
print("CHECK DIAGONAL NEGATIVE")
#board.addPieceAt(Piece('w'), 5, 0)
board.addPieceAt(Piece('w'), 6, 1)
board.addPieceAt(Piece('w'), 7, 2)
board.addPieceAt(Piece('w'), 8, 3)
board.addPieceAt(Piece('w'), 9, 4)
#board.printBoard()
rules = RulesFactory()
if rules.checkForVictoryWithPoint(8, 3, board):
    print("White wins!")
else:
    print("Winner undetermined.")

print()
print("CHECK DIAGONAL POSITIVE")
#board.addPieceAt(Piece('b'), 9, 5)
board.addPieceAt(Piece('b'), 8, 6)
board.addPieceAt(Piece('b'), 7, 7)
board.addPieceAt(Piece('b'), 6, 8)
board.addPieceAt(Piece('b'), 5, 9)
#board.printBoard()
rules = RulesFactory()
if rules.checkForVictoryWithPoint(7, 7, board):
    print("Black wins!")
else:
    print("Winner undetermined.")

print()
board.printBoard()
"""
