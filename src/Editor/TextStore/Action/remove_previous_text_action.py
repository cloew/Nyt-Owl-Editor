from Editor.TextStore.Action.merge_lines_action import MergeLinesAction
from Editor.TextStore.Action.remove_next_text_action import RemoveNextTextAction
from Editor.TextStore.Action.text_store_action import TextStoreAction

class RemovePreviousTextAction(TextStoreAction):
    """ Represents action to remove text """
        
    def do(self):
        """ Perform the action """
        if self.column == 0:
            self.cursor.up()
            self.cursor.toEndOfLine()
        else:
            self.cursor.left()
            
        self.action = RemoveNextTextAction(self.cursor, self.textStore)
        self.action.do()
        
    def undo(self):
        """ Undo the remove tab action """
        self.action.undo()