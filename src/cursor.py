
class Cursor:
    """ Represents the cursor in the text editor """
    
    def __init__(self, textStore):
        """ Initialize the cursor to the beginning of the file """
        self.line = 0
        self.col = 0
        
        self.textStore = textStore
        
    def up(self):
        """ Move the cursor up a line """
        if self.line > 0:
            self.line -= 1
            
        self.normalizeCol()
            
    def down(self, max):
        """ Move the cursor down a line """
        if self.line < self.textStore.lastLine():
            self.line += 1
            
        self.normalizeCol()
            
    def left(self):
        """ Moves the cursor left one column """
        if self.col > 0:
            self.col -= 1
    
    def right(self, max):
        """ Moves the cursor right one column """
        if self.col < self.textStore.lastColumn(self.line):
            self.col += 1
            
    def toStartOfLine(self):
        """ Moves the cursor column to the start of the current line """
        self.col = 0
        
    def toEndOfLine(self):
        """ Moves the cursor column to the end of the current line """
        self.col = self.textStore.lastColumn(self.line)
    
    def normalizeCol(self):
        """ Normalize Column """
        lastCol = self.textStore.lastColumn(self.line)
        
        if self.col > lastCol:
            self.col = lastCol