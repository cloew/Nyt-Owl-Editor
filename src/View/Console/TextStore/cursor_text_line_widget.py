from View.Console.TextStore.text_line_widget import TextLineWidget

class CursorTextLineWidget(TextLineWidget):
    """ Represents the view for a Text Line Widget with the cursor """
    
    def __init__(self, line, lineNumber, textWindow, cursor):
        """ Initialize the view """
        TextLineWidget.__init__(line, lineNumber, textWindow)
        self.cursor = cursor
        
    def draw(self):
        """ Draw the Widget """
        beforeCursor = self.line[self.startCol:self.cursor.col]
        if self.cursor.col < len(self.line):
            cursor = Window.terminal.reverse(self.line[self.cursor.col])
            afterCursor = self.line[self.cursor.col+1:self.endCol]
        else:
            cursor = Window.terminal.reverse(" ")
            afterCursor = ""
            
        self.printTextLine("{0}{1}{2}".format(beforeCursor, cursor, afterCursor))