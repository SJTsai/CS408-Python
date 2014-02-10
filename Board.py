import Piece
import Point

"""Manages the pieces and moves made on the board"""
class Board(object):
    """Initialize board with width and height of specified size
       as well as empty lists for black and white locations on board"""
    def __init__(self, size):
        self.size = size
        self.board = [["-" for i in range(size)] for j in range(size)]
        self.blackLocations = [] """List of Points"""
        self.whiteLocations = [] """List of Points"""
        self.pieceLocations = {"b":self.blackLocations,
                               "w":self.whiteLocations}

    """Add a piece of the specified row and column.
       Raises IllegalMoveError"""
    def addPieceAt(self, piece, point):
        pass

    """Get the piece at specified row and column"""
    def getPieceAt(self, point):
        pass

    """Get the piece locations of a certain color
       (Seems like enums are available in 3.4 but not 3.3.
       Just make sure that color is either 'b' or 'w' """
    def getPieceColorLocations(self, piece):
        return self.pieceLocations[piece.color]

    """Checks if move is valid for given piece"""
    def isLegalFor(self, piece, point):
        pass

    """Check for vertical, horizontal, and diagonal victories."""
    def checkForVictory(self):
        pass

    """Print contents of board"""
    def printBoard(self):
        for row in self.board:
            print(" ".join(row))
        print()
