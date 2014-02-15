from Editor.TextStore.Operation.insert_newline_operation import InsertNewlineOperation
from Editor.TextStore.Operation.merge_lines_operation import MergeLinesOperation

class InsertNewlineAction:
    """ Represents the action to insert a newline in a file """
    
    def __init__(self, cursor, textStore, event=None):
        """ Initialize the newline action """
        self.line = cursor.line
        self.column = cursor.col
        self.cursor = cursor
        self.textStore = textStore
        
    def do(self):
        """ Perform the action """
        operation = InsertNewlineOperation(self.cursor, self.textStore)
        operation.perform()
        
    def undo(self):
        """ Undo the remove tab action """
        self.cursor.line = self.line
        self.cursor.col = self.column
        
        operation = MergeLinesOperation(self.cursor, self.textStore)
        operation.perform()