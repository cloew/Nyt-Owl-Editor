
class InsertNewlineAction:
    """ Represents the action to insert a newline in a file """
    
    def __init__(self, cursor, textStore, event=None):
        """ Initialize the newline action """
        self.line = cursor.line
        self.column = cursor.col
        self.cursor = cursor
        self.textStore = textStore
        
    def do(self):
        """ Perform the action """
        textLine = self.textStore.text[self.line]
        col = self.column
        
        originalLineText = textLine[:col]
        newLineText = textLine[col:]
        self.textStore.text[self.line] = originalLineText
        
        cut = self.line+1
        self.textStore.text[cut:cut] = [newLineText]
        
        self.cursor.down()
        self.cursor.toStartOfLine()
        
    def undo(self):
        """ Undo the remove tab action """