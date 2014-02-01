from kao_gui.console.console_widget import ConsoleWidget

class TextLineWidget(ConsoleWidget):
    """ Represents the view for a Text Line Widget """
    
    def __init__(self, line, lineNumber, textWindow):
        """ Initialize the view """
        lineNumber = str(i)
        self.lineNumber = lineNumber.zfill(maxLength)
        self.line = line
        
        self.startCol = textWindow.left_col
        self.endCol = textWindow.left_col + textWindow.window_width
        
    def draw(self):
        """ Draw the Widget """
        self.printTextLine(self.line[self.startCol:self.endCol])
        
    def printTextLine(self, line):
        """  """
        print "{0}: {1}{t.normal}\r".format(self.lineNumber, line, t=Window.terminal)