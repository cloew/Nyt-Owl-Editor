from Editor.TextStore.Operation.remove_character_operation import RemoveCharacterOperation
from Editor.TextStore.Operation.text_store_operation import TextStoreOperation

class RemoveTabOperation(TextStoreOperation):
    """ Represents operation to remove a tab """
    
    def perform(self):
        """ Perform the Action """
        for i in range(4):
            self.cursor.left()
        operation = RemoveCharacterOperation(self.cursor, self.textStore)
        for i in range(4):
            operation.perform()