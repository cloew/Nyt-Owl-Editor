from Editor.TextStore.Operation.text_store_operation import TextStoreOperation

class InsertTextOperation(TextStoreOperation):
    """ Represents operation to insert text """
    
    def __init__(self, cursor, textStore, textToInsert):
        """ Initialize the operation """
        TextStoreOperation.__init__(self, cursor, textStore)
        self.textToInsert = textToInsert
    
    def perform(self):
        """ Perform the Action """
        self.textStore.text[self.cursor.line] = self.insertTextAtCurrentPosition()
        
        for i in self.textToInsert:
            self.cursor.right()
            
    def insertTextAtCurrentPosition(self):
        """ Insert Text into the line at the current Position """
        textLine = self.textStore.text[self.cursor.line]
        return textLine[:self.cursor.col] + self.textToInsert + textLine[self.cursor.col:]