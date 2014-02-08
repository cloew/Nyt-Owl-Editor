from Editor.TextStore.Action.action_helper import concatenate

class RemoveCharacterAction:
    """ Represents action to remove a character """
    
    def __init__(self, cursor, textStore, event=None):
        """ Initialize the Action """
        self.line = cursor.line
        self.column = cursor.col
        self.cursor = cursor
        self.textStore = textStore
        
    def do(self):
        """ Perform the action """
        textLine = self.textStore.text[self.line]
        col = self.column
        
        self.textStore.text[self.line] = concatenate(textLine, col, col+1)