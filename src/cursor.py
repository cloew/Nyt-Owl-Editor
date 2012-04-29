
class Cursor:
    """ Represents the cursor in the text editor """
    
    def __init__(self):
        """ Initialize the cursor to the beginning of the file """
        self.line = 0
        self.col = 0
        
    def up(self):
        """ Move the cursor up a line """
        if self.line > 0:
            self.line -= 1
            
    def down(self, max):
        """ Move the cursor down a line """
        if self.line < max - 1:
            self.line += 1
            
    def left(self):
        """ Moves the cursor left one column """
        if self.col > 0:
            self.col -= 1
    
    def right(self, max):
        """ Moves the cursor right one column """
        if self.col < max:
            self.col += 1
    