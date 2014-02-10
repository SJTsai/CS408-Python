class Point(object):
    """Initialize Point with specified row and column"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

<<<<<<< Updated upstream
    """Return the x (row) position of the Point"""
    def getX():
        return self.x
    
    """Return the y (column) position of the Point"""
    def getY():
        return self.y
=======
    def __repr__(self):
        return "(%d, %d)" % (self.x, self.y)
>>>>>>> Stashed changes
