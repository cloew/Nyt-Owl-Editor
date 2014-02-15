from Editor.TextStore.Action.text_store_action import TextStoreAction

from Editor.TextStore.Operation.insert_newline_operation import InsertNewlineOperation
from Editor.TextStore.Operation.merge_lines_operation import MergeLinesOperation

class InsertNewlineAction(TextStoreAction):
    """ Represents the action to insert a newline in a file """
        
    def performDoOperation(self):
        """ Perform the action """
        operation = InsertNewlineOperation(self.cursor, self.textStore)
        operation.perform()
        
    def performUndoOperation(self):
        """ Undo the insert newline """
        operation = MergeLinesOperation(self.cursor, self.textStore)
        operation.perform()