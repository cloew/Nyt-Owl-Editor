
class RemovePreviousTextAction:
    """ Represents action to remove text """
    
    def __init__(self, cursor, textStore, event=None):
        """ Initialize the Action """
        self.line = cursor.line
        self.column = cursor.col
        self.cursor = cursor
        self.textStore = textStore
        
    def do(self):
        """ Perform the action """
        if self.column == 0:
            self.removeLine()
        else:
            self.removeChar()
        
    def removeChar(self):
        """ Removes a character from a line """
        textLine = self.textStore.text[self.line]
        col = self.column
        
        self.textStore.text[self.line] = self.concatenate(textLine, col-1, col)
        self.cursor.left()
        
    def removeLine(self):
        """ Removes a line and appends the extra characters to the line above """
        if self.line == 0:
            return
            
        self.cursor.toEndOfLine(self.line-1)
        
        line = self.textStore.text[self.line]
        self.textStore.text[self.line-1] += line
        self.textStore.text = self.concatenate(self.textStore.text, self.line, self.line+1, filler = [])
        
        self.cursor.up()
        
    def concatenate(self, toCut, firstCut, lastCut, filler = ""):
        return toCut[:firstCut] + filler + toCut[lastCut:]