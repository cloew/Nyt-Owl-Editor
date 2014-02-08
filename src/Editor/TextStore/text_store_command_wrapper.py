from Editor.TextStore.Action.insert_newline_action import InsertNewlineAction
from Editor.TextStore.Action.insert_tab_action import InsertTabAction
from Editor.TextStore.Action.insert_text_action import InsertTextAction
from Editor.TextStore.Action.remove_next_text_action import RemoveNextTextAction
from Editor.TextStore.Action.remove_previous_text_action import RemovePreviousTextAction

class TextStoreCommandWrapper:
    """ Wrapper for Text Store Commands """
    
    def __init__(self, parent):
        """ Initialize the Cursor Command Wrapper with its parent """
        self.cursor = parent.cursor
        self.textStore = parent.textStore
        self.addCommandsToParent(parent)
        
    def addCommandsToParent(self, parent):
        """ Add commands to the parent """
        commands = ["addString", "addLine", "addTab", "remove",
                    "delete"]
        
        for command in commands:
            setattr(parent, command, getattr(self, command))
        
    def currentLine(self):
        """ Returns the current line """
        return self.textStore.text[self.cursor.line]
                
    def addString(self, toAdd):
        """ Adds a string at the current cursor """
        action = InsertTextAction(self.cursor, self.textStore, toAdd)
        action.do()
        
    def addLine(self, event=None):
        """ Adds a new line to the file """
        action = InsertNewlineAction(self.cursor, self.textStore)
        action.do()
        
    def addTab(self, event=None):
        """ Adds a Tab at the current cursor location """
        action = InsertTabAction(self.cursor, self.textStore)
        action.do()
        
    def remove(self, event=None):
        """ Removes a character from the line """
        action = RemovePreviousTextAction(self.cursor, self.textStore)
        action.do()
            
    def delete(self, event=None):
        """ Deletes a character """
        action = RemoveNextTextAction(self.cursor, self.textStore)
        action.do()
            
    def removeChar(self):
        """ Removes a character from a line """
        line = self.textStore.text[self.cursor.line]
        col = self.cursor.col
        
        self.textStore.text[self.cursor.line] = self.concatenate(line, col-1, col)
        self.cursor.left()
        
    def removeLine(self):
        """ Removes a line and appends the extra characters to the line above """
        if self.cursor.line == 0:
            return
        
        line = self.textStore.text[self.cursor.line]
        
        self.cursor.col = len(self.textStore.text[self.cursor.line-1])
        
        self.textStore.text[self.cursor.line-1] += line
        
        self.textStore.text = self.concatenate(self.textStore.text, self.cursor.line, self.cursor.line+1, filler = [])
        self.cursor.up()
        
    def concatenate(self, toCut, firstCut, lastCut, filler = ""):
        return toCut[:firstCut] + filler + toCut[lastCut:]