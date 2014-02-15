from Editor.TextStore.Operation.operation_helper import concatenate
from Editor.TextStore.Operation.text_store_operation import TextStoreOperation

class RemoveCharacterOperation(TextStoreOperation):
    """ Represents operation to remove a character """
    
    def perform(self):
        """ Perform the Action """
        textLine = self.textStore.text[self.cursor.line]
        col = self.cursor.col
        
        self.textStore.text[self.cursor.line] = concatenate(textLine, col, col+1)