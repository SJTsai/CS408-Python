from Color import Color
from Piece import Piece
from Point import Point

"""Manages the pieces and moves made on the board"""
class Board(object):
    """Initialize board with width and height of specified size
       as well as empty lists for black and white locations on board"""
    def __init__(self, size):
        self.size = size
        """Make the board list"""
        self.board = [["-" for i in range(size)] for j in range(size)]
        """List of points for black and white inside a dictionary"""
        self.pieceLocations = {Color.black:[], Color.white:[]}
        
    """Add a piece of the specified row and column.
       Raises IllegalMoveError"""
    def addPieceAt(self, piece, point):
        """Check if point is valid here"""
        
        if piece.color == Color.black:
            self.pieceLocations[Color.black].append(point)
        elif piece.color == Color.white:
            self.pieceLocations[Color.white].append(point)

        self.board[point.x][point.y] = piece.color

    """Get the piece at specified row and column"""
    def getPieceAt(self, point):
        """Check if point is valid here"""
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

    def printBlackLocations(self):
        for point in self.pieceLocations[Color.black]:
            print(point)

    def printWhiteLocations(self):
        for point in self.pieceLocations[Color.white]:
            print(point)
