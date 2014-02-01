from kao_gui.console.console_widget import ConsoleWidget
from kao_gui.console.window import Window

class TextLineWidget(ConsoleWidget):
    """ Represents the view for a Text Line Widget """
    
    def __init__(self, line, lineNumber, textWindow):
        """ Initialize the view """
        self.lineNumber = lineNumber
        self.line = line
        
        self.startCol = textWindow.left_col
        self.endCol = textWindow.right_col
        
    def draw(self):
        """ Draw the Widget """
        self.printTextLine(self.line[self.startCol:self.endCol])
        
    def printTextLine(self, line):
        """ Print the given text line with a line number """
        text = "{0}: {1}".format(self.lineNumber, line)
        text = text.replace('\r', '')
        print "{0}{t.normal}\r".format(text, t=Window.terminal)