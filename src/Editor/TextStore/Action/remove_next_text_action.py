from Editor.TextStore.Action.merge_lines_action import MergeLinesAction
from Editor.TextStore.Action.remove_character_action import RemoveCharacterAction
from Editor.TextStore.Action.text_store_action import TextStoreAction

class RemoveNextTextAction(TextStoreAction):
    """ Represents an action to remove the next character """
        
    def do(self):
        """ Perform the action """
        if self.column == len(self.textStore.text[self.line]):
            self.removeLine()
        else:
            self.removeChar()
        
    def removeChar(self):
        """ Removes a character from a line """
        self.action = RemoveCharacterAction(self.cursor, self.textStore)
        self.action.do()
        
    def removeLine(self):
        """ Removes a line and appends the extra characters to the line above """
        self.action = MergeLinesAction(self.cursor, self.textStore)
        self.action.do()
        
    def undo(self):
        """ Undo the remove next text action """
        self.action.undo()