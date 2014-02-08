
class MergeLinesAction:
    """ Action to merge a line with its next line """
    
    def __init__(self, cursor, textStore, event=None):
        """ Initialize the Action """
        self.line = cursor.line
        self.column = cursor.col
        self.cursor = cursor
        self.textStore = textStore
        
    def do(self):
        """ Perform the action """
        if self.line == self.textStore.lastLine:
            return
        
        nextLineText = self.textStore.text[self.line+1]
        self.textStore.text[self.line] += nextLineText
        self.textStore.text = self.concatenate(self.textStore.text, self.line+1, self.line+2, filler = [])
        
    def concatenate(self, toCut, firstCut, lastCut, filler = ""):
        return toCut[:firstCut] + filler + toCut[lastCut:]