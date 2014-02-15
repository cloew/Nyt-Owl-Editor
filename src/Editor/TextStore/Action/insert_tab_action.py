from Editor.TextStore.Action.text_store_action import TextStoreAction

from Editor.TextStore.Operation.insert_tab_operation import InsertTabOperation
from Editor.TextStore.Operation.remove_tab_operation import RemoveTabOperation

class InsertTabAction(TextStoreAction):
    """ Represents action to insert a tab """
        
    def do(self):
        """ Perform the action """
        operation = InsertTabOperation(self.cursor, self.textStore)
        operation.perform()
        
    def performUndoOperation(self):
        """ Undo the insert tab action """
        operation = RemoveTabOperation(self.cursor, self.textStore)
        operation.perform()