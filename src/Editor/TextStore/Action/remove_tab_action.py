from Editor.TextStore.Action.text_store_action import TextStoreAction

from Editor.TextStore.Operation.insert_tab_operation import InsertTabOperation
from Editor.TextStore.Operation.remove_tab_operation import RemoveTabOperation

class RemoveTabAction(TextStoreAction):
    """ Action to remove a tab """
    
    def isDoable(self):
        """ Return if the action can be done """
        return not (self.column == 0)
        
    def performDoOperation(self):
        """ Perform the action """
        operation = RemoveTabOperation(self.cursor, self.textStore, self.settings)
        operation.perform()
            
    def performUndoOperation(self):
        """ Undo the remove tab action """
        operation = InsertTabOperation(self.cursor, self.textStore, self.settings)
        operation.perform()