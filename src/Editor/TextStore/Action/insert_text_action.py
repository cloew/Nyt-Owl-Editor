from Editor.TextStore.Action.text_store_action import TextStoreAction

from Editor.TextStore.Operation.insert_text_operation import InsertTextOperation
from Editor.TextStore.Operation.remove_character_operation import RemoveCharacterOperation

class InsertTextAction(TextStoreAction):
    """ Represents an Action to insert text into the text store """
    
    def __init__(self, cursor, textStore, textToInsert):
        """ Initialize the Insert Text Action """
        self.textToInsert = textToInsert
        TextStoreAction.__init__(self, cursor, textStore)
        
    def isDoable(self):
        """ Return if the action can be done """
        return True
        
    def performDoOperation(self):
        """ Perform the action """
        operation = InsertTextOperation(self.cursor, self.textStore, self.textToInsert)
        operation.perform()
        
    def performUndoOperation(self):
        """ Undo the inserted text """
        operation = RemoveCharacterOperation(self.cursor, self.textStore)
        for character in self.textToInsert:
            operation.perform()