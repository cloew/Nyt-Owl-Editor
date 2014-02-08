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