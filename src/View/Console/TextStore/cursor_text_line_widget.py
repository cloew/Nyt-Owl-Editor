from View.Console.TextStore.text_line_widget import TextLineWidget

class CursorTextLineWidget(TextLineWidget):
    """ Represents the view for a Text Line Widget with the cursor """
    
    def __init__(self, line, lineNumber, textWindow, settings, cursor):
        """ Initialize the view """
        TextLineWidget.__init__(self, line, lineNumber, textWindow, settings)
        self.cursor = cursor
        
    def draw(self):
        """ Draw the Widget """
        beforeCursor = self.line[self.startCol:self.cursor.col]
        if self.cursor.col < len(self.line):
            cursor = self.terminal.reverse(self.line[self.cursor.col])
            afterCursor = self.line[self.cursor.col+1:self.endCol]
        else:
            cursor = self.terminal.reverse(" ")
            afterCursor = ""
            
        self.printTextLine("{0}{1}{2}".format(beforeCursor, cursor, afterCursor))