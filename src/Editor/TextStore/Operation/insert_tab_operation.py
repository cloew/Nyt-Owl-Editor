from Editor.TextStore.Operation.insert_text_operation import InsertTextOperation
from Editor.TextStore.Operation.text_store_operation import TextStoreOperation

class InsertTabOperation(TextStoreOperation):
    """ Represents operation to insert a tab """
    
    def __init__(self, cursor, textStore, settings):
        """ Initialize the operation """
        TextStoreOperation.__init__(self, cursor, textStore)
        self.settings = settings
    
    def perform(self):
        """ Perform the Action """
        spacesToAdd = self.settings.tabSize-self.cursor.col%self.settings.tabSize
        insertTextOperation = InsertTextOperation(self.cursor, self.textStore, " "*spacesToAdd)
        insertTextOperation.perform()