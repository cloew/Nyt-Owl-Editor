
class Cursor:
    """ Represents the cursor in the text editor """
    
    def __init__(self, textStore):
        """ Initialize the cursor to the beginning of the file """
        self.line = 0
        self.col = 0
        
        self.textStore = textStore
        
    def up(self):
        """ Move the cursor up a line """
        self.jumpDown(-1)
            
    def jumpUp(self, linesToJump):
        """ Jumps the cursor down the given number of lines """
        self.jumpDown(-1*linesToJump)

    def down(self):
        """ Move the cursor down a line """
        self.jumpDown(1)

    def jumpDown(self, linesToJump):
        """ Jumps the cursor down the given number of lines """
        self.line += linesToJump
        self.line = max(self.line, 0)
        self.line = min(self.line, self.textStore.lastLine())

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
        
    def toEndOfFile(self):
        """ Move the cursor to the end of the file """
        self.toBottomOfFile()
        self.toEndOfLine()
        
    def toTopOfFile(self):
        """ Move the cursor row to the top line of the file """
        self.jumpDown(-1*self.textStore.lastLine())
        
    def toBottomOfFile(self):
        """ Move the cursor row to the bottom line of the file """
        self.jumpDown(self.textStore.lastLine())
            
    def toStartOfLine(self):
        """ Moves the cursor column to the start of the current line """
        self.col = 0
        
    def toEndOfLine(self, line=None):
        """ Moves the cursor column to the end of the current line """
        if line is None:
            line = self.line
        self.col = self.textStore.lastColumn(line)
        
    def toPreviousWord(self):
        """ Move the cursor to the start of the previous word """
        foundPotentialStartOfWord = False
        restOfLine = list(self.textStore.text[self.line][:self.col])
        restOfLine.reverse()
        for character in restOfLine:
            if character != ' ':
                foundPotentialStartOfWord = True
            elif foundPotentialStartOfWord and character == ' ':
                break
            self.left()
        
    def toNextWord(self):
        """ Move the cursor to the start of the next word """
        foundPotentialCharacterBeforeWord = False
        for character in self.textStore.text[self.line][self.col:]:
            if character == ' ':
                foundPotentialCharacterBeforeWord = True
            elif foundPotentialCharacterBeforeWord and character != ' ':
                break
            self.right()
    
    def normalizeCol(self):
        """ Normalize Column """
        lastCol = self.textStore.lastColumn(self.line)
        
        if self.col > lastCol:
            self.col = lastCol