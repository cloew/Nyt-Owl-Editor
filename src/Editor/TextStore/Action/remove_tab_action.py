from Editor.TextStore.Action.remove_character_action import RemoveCharacterAction

class RemoveTabAction:
    """ Action to remove a tab """
    
    def __init__(self, cursor, textStore, event=None):
        """ Initialize the Action """
        self.line = cursor.line
        self.column = cursor.col
        self.cursor = cursor
        self.textStore = textStore
        
    def do(self):
        """ Perform the action """
        for i in range(4):
            self.cursor.left()
        action = RemoveCharacterAction(self.cursor, self.textStore)
        for i in range(4):
            action.do()
            
    def undo(self):
        """ Undo the remove tab action """