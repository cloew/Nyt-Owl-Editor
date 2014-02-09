from Editor.TextStore.Action.merge_lines_action import MergeLinesAction
from Editor.TextStore.Action.remove_character_action import RemoveCharacterAction

class RemoveNextTextAction:
    """ Represents an action to remove the next character """
    
    def __init__(self, cursor, textStore, event=None):
        """ Initialize the Action """
        self.line = cursor.line
        self.column = cursor.col
        self.cursor = cursor
        self.textStore = textStore
        
    def do(self):
        """ Perform the action """
        if self.column == len(self.textStore.text[self.line]):
            self.removeLine()
        else:
            self.removeChar()
        
    def removeChar(self):
        """ Removes a character from a line """
        action = RemoveCharacterAction(self.cursor, self.textStore)
        action.do()
        
    def removeLine(self):
        """ Removes a line and appends the extra characters to the line above """
        action = MergeLinesAction(self.cursor, self.textStore)
        action.do()
        
    def undo(self):
        """ Undo the remove tab action """