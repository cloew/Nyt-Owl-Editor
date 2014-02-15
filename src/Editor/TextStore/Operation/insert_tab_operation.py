from Editor.TextStore.Operation.insert_text_operation import InsertTextOperation
from Editor.TextStore.Operation.text_store_operation import TextStoreOperation

class InsertTabOperation(TextStoreOperation):
    """ Represents operation to insert a tab """
    
    def perform(self):
        """ Perform the Action """
        insertTextOperation = InsertTextOperation(self.cursor, self.textStore, " "*4)
        insertTextAction.do()