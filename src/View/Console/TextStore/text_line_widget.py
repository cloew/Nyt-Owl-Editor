from kao_gui.console.console_widget import ConsoleWidget

class TextLineWidget(ConsoleWidget):
    """ Represents the view for a Text Line Widget """
    
    def __init__(self, line, lineNumber, textWindow, settings):
        """ Initialize the view """
        self.lineNumber = lineNumber
        self.line = line
        self.settings = settings
        
        self.startCol = textWindow.left_col
        self.endCol = textWindow.right_col
        
    def draw(self):
        """ Draw the Widget """
        self.printTextLine(self.line[self.startCol:self.endCol])
        
    def printTextLine(self, line):
        """ Print the given text line with a line number """
        # for keyword in self.settings.keywords:
            # line = line.replace(keyword, "{t.green}{0}{t.normal}".format(keyword, t=self.terminal))
        
        text = "{0}: {1}".format(self.lineNumber, line)
        text = text.replace('\r', '')
        print "{0}{t.normal}\r".format(text, t=self.terminal)