
class TextStoreAction:
    """ Represents a text store action """
    
    def __init__(self, cursor, textStore, event=None):
        """ Initialize the Action """
        self.line = cursor.line
        self.column = cursor.col
        self.cursor = cursor
        self.textStore = textStore
        
    def do(self):
        """ Perform the action """
        
    def undo(self):
        """ Undo the action """
        self.resetCursor()
        self.performUndoOpertaion()
        
    def performUndoOperation(self):
        """ Perform the undo operation """
        
    def resetCursor(self):
        """ Place the cursor back where the action occured """
        self.cursor.line = self.line
        self.cursor.col = self.column