class Piece(object):

    """ Use 'b' or 'w' for color for the purposes of this project """
    def __init__(self, color):
        self.color = color

    """ Returns 'b' or 'w' for the Piece color """
    def getColor():
        return self.color

    def __repr__(self):
        return "Piece color: %s" % self.color
