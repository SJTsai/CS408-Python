class Piece(object):
    """Use Color.black or Color.white for color for
       the purposes of this project."""
    def __init__(self, color):
        self.color = color

    """
        Returns this piece's color
        returns: Character. Either 'b' or 'w'.
    """
    def getColor(self):
        return self.color
