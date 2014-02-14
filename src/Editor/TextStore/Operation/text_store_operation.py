
class TextStoreOperation:
    """ Represents an atomic Text Store Operation """
    
    def __init__(self, cursor, textStore):
        """ Initialize the operation """
        self.cursor = cursor
        self.textStore = textStore
        
    def perform(self):
        """ Perform the operation """