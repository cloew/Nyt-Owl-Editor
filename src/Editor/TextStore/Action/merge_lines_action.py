from Editor.TextStore.Action.text_store_action import TextStoreAction

from Editor.TextStore.Operation.insert_newline_operation import InsertNewlineOperation
from Editor.TextStore.Operation.merge_lines_operation import MergeLinesOperation

class MergeLinesAction(TextStoreAction):
    """ Action to merge a line with its next line """
    
    def isDoable(self):
        """ Return if the action can be done """
        return True
        
    def performDoOperation(self):
        """ Perform the action """
        operation = MergeLinesOperation(self.cursor, self.textStore)
        operation.perform()
        
    def performUndoOperation(self):
        """ Undo the merge lines action """
        operation = InsertNewlineOperation(self.cursor, self.textStore)
        operation.perform()
        