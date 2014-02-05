from Editor.Cursor.cursor import Cursor
from Editor.Cursor.cursor_command_wrapper import CursorCommandWrapper
from Editor.TextStore.text_store import TextStore
from Editor.TextStore.text_store_command_wrapper import TextStoreCommandWrapper

import os

class NytOwlTextEditor:
    """ The NytOwl Text Editor """
    
    def __init__(self, filename, textWindow):
        """  """
        self.filename = filename
        self.textWindow = textWindow
        
        self.textStore = TextStore(filename)
        self.cursor = Cursor(self.textStore)
        
        self.cursorCommandWrapper = CursorCommandWrapper(self) 
        self.textStoreCommandWrapper = TextStoreCommandWrapper(self)
        
    def save(self, event=None):
        """  """
        if self.noFile():
            self.filename = str(raw_input("Enter filename to save to: "))
        
        try:
            file = open(self.filename, 'w')
            for line in self.textStore.text:
                file.write(line + "\n")
            file.close()
        except IOError:
            print "Unable to open file"
            
    def noFile(self):
        return self.filename is None

    @property
    def base_filename(self):
        """ Return the File's basename """
        if self.filename is None:
            return None
        else:
            return os.path.basename(self.filename)