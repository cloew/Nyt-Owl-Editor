from Editor.TextStore.Action.text_store_action import TextStoreAction

from Editor.TextStore.Operation.insert_text_operation import InsertTextOperation
from Editor.TextStore.Operation.remove_character_operation import RemoveCharacterOperation

class RemoveCharacterAction(TextStoreAction):
    """ Represents action to remove a character """
    
    def isDoable(self):
        """ Return if the action can be done """
        return True
        
    def performDoOperation(self):
        """ Perform the action """
        textLine = self.textStore.text[self.line]
        col = self.column
        self.removedCharacter = textLine[col]
        
        operation = RemoveCharacterOperation(self.cursor, self.textStore)
        operation.perform()
        
    def performUndoOperation(self):
        """ Undo the remove character action """
        operation = InsertTextOperation(self.cursor, self.textStore, self.removedCharacter)
        operation.perform()