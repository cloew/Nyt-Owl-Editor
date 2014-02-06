
class InsertTextAction:
    """ Represents an Action to insert text into the text store """
    
    def __init__(self, cursor, textStore, textToInsert):
        """ Initialize the Insert Text Action """
        self.line = cursor.line
        self.column = cursor.col
        self.cursor = cursor
        self.textStore = textStore
        self.textToInsert = textToInsert
        
    def do(self):
        """ Perform the action """
        self.textStore.text[self.line] = self.insertTextAtCurrentPosition()
        
        for i in self.textToInsert:
            self.cursor.right()
        
    def insertTextAtCurrentPosition(self):
        """ Insert Text into the line at the current Position """
        textLine = self.textStore.text[self.line]
        return textLine[:self.column] + self.textToInsert + textLine[self.column:]