
class CursorCommandWrapper:
    """ Wrapper for the Cursor Commands """
    
    def __init__(self, parent):
        """ Initialize the Cursor Command Wrapper with its parent """
        self.cursor = parent.cursor
        self.textWindow = parent.textWindow
        self.addCommandsToParent(parent)
        
    def addCommandsToParent(self, parent):
        """ Add commands to the parent """
        commands = ["cursorUp", "cursorDown", "cursorLeft", "cursorRight",
                    "cursorStart", "cursorEnd", "cursorPageUp", "cursorPageDown",
                    "cursorStartOfFile", "cursorEndOfFile", "cursorPreviousWord",
                    "cursorNextWord"]
        
        for command in commands:
            setattr(parent, command, getattr(self, command))
        
    def cursorUp(self, event=None):
        """ Moves cursor up one line """
        self.cursor.up()
        
    def cursorDown(self, event=None):
        """ Moves cursor down one line """
        self.cursor.down()
    
    def cursorLeft(self, event=None):
        """ Moves cursor left one column """
        self.cursor.left()
        
    def cursorRight(self, event=None):
        """ Moves cursor right one column """
        self.cursor.right()
        
    def cursorStart(self, event=None):
        """ Move cursor to the start of the line """
        self.cursor.toStartOfLine()
        
    def cursorEnd(self, event=None):
        """ Move cursor to the end of the line """
        self.cursor.toEndOfLine()

    def cursorPageUp(self, event=None):
        """ Move the cursor up a page """
        self.cursor.jumpUp(self.textWindow.window_height)
        self.textWindow.top_line = self.cursor.line

    def cursorPageDown(self, event=None):
        """ Move the cursor down a page """
        self.cursor.jumpDown(self.textWindow.window_height)
        self.textWindow.top_line = self.cursor.line
        
    def cursorStartOfFile(self, event=None):
        """ Move the cursor to the start of the file """
        self.cursor.toStartOfFile()
        
    def cursorEndOfFile(self, event=None):
        """ Move the cursor to the start of the file """
        self.cursor.toEndOfFile()
        
    def cursorPreviousWord(self, event=None):
        """ Move the cursor to the previous word """
        self.cursor.toPreviousWord()
        
    def cursorNextWord(self, event=None):
        """ Move the cursor to the next word """
        self.cursor.toNextWord()
