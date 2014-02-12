from Editor.TextStore.Action.insert_text_action import InsertTextAction

class InsertTabAction:
    """ Represents action to insert a tab """
    
    def __init__(self, cursor, textStore, event=None):
        """ Initialize the Action """
        self.line = cursor.line
        self.column = cursor.col
        self.cursor = cursor
        self.textStore = textStore
        self.insertTextAction = None
        
    def do(self):
        """ Perform the action """
        self.insertTextAction = InsertTextAction(self.cursor, self.textStore, " "*4)
        self.insertTextAction.do()
        
    def undo(self):
        """ Undo the remove tab action """
        self.cursor.line = self.line
        self.cursor.col = self.column
        
        if self.insertTextAction is not None:
            self.insertTextAction.undo()