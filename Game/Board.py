from Piece import Piece

""" Manages the pieces and the moves made on the board """
class Board(object):
    
    """ Initialize board with width and height of specified size """
    def __init__(self, size):
        self.size = size
        self.board = [[None for i in range(size)] for j in range(size)]

    def getSize(self):
        return self.size

    def getBoard(self):
        return self.board
        
    """ Add a piece of the specified row and column. """
    def addPieceAt(self, piece, row, col):
        if self.isOutOfBounds(row, col):
            return False
        
        self.board[row][col] = piece
        return True

    """ Get the piece at specified row and column """
    def getPieceAt(self, row, col):
        if self.isOutOfBounds(row, col):
            return None

        return self.board[row][col]

    def isOutOfBounds(self, row, col):
        return row < 0 or row >= self.size or col < 0 or col >= self.size
    
    """Print contents of board"""
    def printBoard(self):
        for row in self.board:
            for piece in row:
                if piece is None:
                    string = '-'
                else:
                    string = piece.color
                print(string, end = " ")
            print()
