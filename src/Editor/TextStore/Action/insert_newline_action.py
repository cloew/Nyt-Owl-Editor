from Editor.TextStore.Action.merge_lines_action import MergeLinesAction

from Editor.TextStore.Operation.insert_newline_operation import InsertNewlineOperation

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
        
        # textLine = self.textStore.text[self.line]
        # col = self.column
        
        # originalLineText = textLine[:col]
        # newLineText = textLine[col:]
        # self.textStore.text[self.line] = originalLineText
        
        # cut = self.line+1
        # self.textStore.text[cut:cut] = [newLineText]
        
        # self.cursor.down()
        # self.cursor.toStartOfLine()
        
    def undo(self):
        """ Undo the remove tab action """
        self.cursor.line = self.line
        self.cursor.col = self.column
        
        action = MergeLinesAction(self.cursor, self.textStore)
        action.do()