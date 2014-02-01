
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
            
    def jumpUp(self, linesToJump):
        """ Jumps the cursor down the given number of lines """
        if (self.line-linesToJump) > 0:
            self.line -= linesToJump
        else:
            self.line = 0

        self.normalizeCol()

    def down(self):
        """ Move the cursor down a line """
        if self.line < self.textStore.lastLine():
            self.line += 1
            
        self.normalizeCol()

    def jumpDown(self, linesToJump):
        """ Jumps the cursor down the given number of lines """
        if (self.line+linesToJump) < self.textStore.lastLine():
            self.line += linesToJump
        else:
            self.line = self.textStore.lastLine()

        self.normalizeCol()
            
    def left(self):
        """ Moves the cursor left one column """
        if self.col > 0:
            self.col -= 1
    
    def right(self):
        """ Moves the cursor right one column """
        if self.col < self.textStore.lastColumn(self.line):
            self.col += 1
            
    def toStartOfFile(self):
        """ Move the cursor to the start of the file """
        self.toStartOfLine()
        self.toTopOfFile()
        
    def toTopOfFile(self):
        """ Move the cursor row to the top line of the file """
        self.line = 0
            
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