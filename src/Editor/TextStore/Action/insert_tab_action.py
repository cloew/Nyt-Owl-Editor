from Editor.TextStore.Action.insert_text_action import InsertTextAction

class InsertTabAction:
    """ Represents action to insert a tab """
    
    def __init__(self, cursor, textStore, event=None):
        """ Initialize the Action """
        self.line = cursor.line
        self.column = cursor.col
        self.cursor = cursor
        self.textStore = textStore
        
    def do(self):
        """ Perform the action """
        insertTextAction = InsertTextAction(self.cursor, self.textStore, " "*4)
        insertTextAction.do()