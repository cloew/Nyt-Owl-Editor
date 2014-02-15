from Editor.TextStore.Operation.text_store_operation import TextStoreOperation

class InsertNewlineOperation(TextStoreOperation):
    """ Represents operation to insert a newline """
    
    def perform(self):
        """ Perform the Action """
        textLine = self.textStore.text[self.cursor.line]
        col = self.cursor.col
        
        originalLineText = textLine[:col]
        newLineText = textLine[col:]
        
        self.textStore.text[self.cursor.line] = originalLineText
        self.insertNewLine(newLineText)
        
        self.cursor.down()
        self.cursor.toStartOfLine()
        
    def insertNewLine(self, newLineText):
        """ Insert the New Line Text as the next line in the text store """
        nextLine = self.cursor.line+1
        self.textStore.text[cut:cut] = [newLineText]