from Editor.Settings.settings import Settings

from Editor.TextStore.Operation.remove_character_operation import RemoveCharacterOperation
from Editor.TextStore.Operation.text_store_operation import TextStoreOperation

class RemoveTabOperation(TextStoreOperation):
    """ Represents operation to remove a tab """
    
    def __init__(self, cursor, textStore, settings):
        """ Initialize the operation """
        TextStoreOperation.__init__(self, cursor, textStore)
        self.settings = settings
    
    def perform(self):
        """ Perform the Action """
        if self.settings.tabStyle is Settings.HARD_TABS:
            self.removeHardTab()
        else:
            self.removeSoftTab()
        
    def removeHardTab(self):
        """ Remove a tab """
        self.cursor.left()
        operation = RemoveCharacterOperation(self.cursor, self.textStore)
        operation.perform()
        
    def removeSoftTab(self):
        """ Remove a space-based tab """
        for i in range(self.settings.tabSize):
            self.cursor.left()
        operation = RemoveCharacterOperation(self.cursor, self.textStore)
        for i in range(self.settings.tabSize):
            operation.perform()