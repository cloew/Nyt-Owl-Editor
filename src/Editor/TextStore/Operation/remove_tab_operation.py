from Editor.TextStore.Operation.remove_character_operation import RemoveCharacterOperation
from Editor.TextStore.Operation.text_store_operation import TextStoreOperation

class RemoveTabOperation(TextStoreOperation):
    """ Represents operation to remove a tab """
    
    def __init__(self, cursor, textStore, settings):
        """ Initialize the operation """
        TextStoreOperation.__init__(self, cursor, textStore)
        self.settings = settings
    
    def perform(self):
        """ Perform the Action """
        for i in range(self.settings.tabSize):
            self.cursor.left()
        operation = RemoveCharacterOperation(self.cursor, self.textStore)
        for i in range(self.settings.tabSize):
            operation.perform()