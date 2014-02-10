class Piece(object):

    """Use 'b' or 'w' for color for the purposes of this project"""
    def __init__(self, color):
        self.color = color

    def printColor(self):
        print(self.color)
