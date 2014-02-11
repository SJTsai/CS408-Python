class Piece(object):

    """Use 'b' or 'w' for color for the purposes of this project"""
    def __init__(self, color):
        self.color = color

    """
        Returns this piece's color
        returns: Character. Either 'b' or 'w'.
    """
    def getColor():
        return self.color
        
    def printColor(self):
        print(self.color)
