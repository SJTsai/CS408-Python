"""Implementation of Connect 5 rules"""
import Board

class RulesFactory(object):
    
    def __init__(self, size):
        self.size = size

    """
        Return True if the color wins, False otherwise.
    """
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
                