from Editor.TextStore.Action.insert_newline_action import InsertNewlineAction
from Editor.TextStore.Action.insert_tab_action import InsertTabAction
from Editor.TextStore.Action.insert_text_action import InsertTextAction
from Editor.TextStore.Action.remove_next_text_action import RemoveNextTextAction
from Editor.TextStore.Action.remove_previous_text_action import RemovePreviousTextAction
from Editor.TextStore.Action.remove_tab_action import RemoveTabAction

class TextStoreCommandWrapper:
    """ Wrapper for Text Store Commands """
    
    def __init__(self, parent):
        """ Initialize the Cursor Command Wrapper with its parent """
        self.cursor = parent.cursor
        self.textStore = parent.textStore
        self.lastAction = None
        self.addCommandsToParent(parent)
        
    def addCommandsToParent(self, parent):
        """ Add commands to the parent """
        commands = {"addString":InsertTextAction,
                    "addLine":InsertNewlineAction,
                    "addTab":InsertTabAction,
                    "remove":RemovePreviousTextAction,
                    "delete":RemoveNextTextAction,
                    "removeTab":RemoveTabAction}
                    
        for command in commands:
            actionClass = commands[command]
            actionFunction = self.makeTextStoreActionEventFunction(actionClass)
            setattr(self, command, actionFunction)
            setattr(parent, command, getattr(self, command))
            
        parent.undo = self.undo
            
    def makeTextStoreActionEventFunction(self, actionClass):
        def performAction(event):
            action = actionClass(self.cursor, self.textStore, event)
            action.do()
            self.lastAction = action
        return performAction
        
    def undo(self, event=None):
        """ Undo the previous action """
        if self.lastAction is not None:
            self.lastAction.undo()
            self.lastAction = None