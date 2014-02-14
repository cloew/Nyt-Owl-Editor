from Editor.TextStore.Action.action_helper import concatenate
from Editor.TextStore.Operation.text_store_operation import TextStoreOperation

class MergeLinesOperation(TextStoreOperation):
    """ Represents operation to merge lines """
    
    def perform(self):
        """ Perform the Action """
        nextLineText = self.textStore.text[self.line+1]
        self.textStore.text[self.line] += nextLineText
        self.textStore.text = concatenate(self.textStore.text, self.line+1, self.line+2, filler = [])