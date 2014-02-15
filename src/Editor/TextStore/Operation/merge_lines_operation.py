from Editor.TextStore.Action.action_helper import concatenate
from Editor.TextStore.Operation.text_store_operation import TextStoreOperation

class MergeLinesOperation(TextStoreOperation):
    """ Represents operation to merge lines """
    
    def perform(self):
        """ Perform the Action """
        line = self.cursor.line
        
        nextLineText = self.textStore.text[line+1]
        self.textStore.text[line] += nextLineText
        self.textStore.text = concatenate(self.textStore.text, line+1, line+2, filler = [])