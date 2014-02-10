class Piece(object):
    """Use Color.black or Color.white for color for
       the purposes of this project."""
    def __init__(self, color):
        self.color = color

    def printColor(self):
        print(self.color)
