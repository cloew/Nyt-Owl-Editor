from text_window import TextWindow

from kao_gui.console.console_widget import ConsoleWidget
from kao_gui.console.window import Window

class TextWidget(ConsoleWidget):
    """ Represents the view for a *** """
    
    def __init__(self, textStore, cursor):
        """ Initialize the view """
        self.cursor = cursor
        self.textStore = textStore
        self.textWindow = TextWindow()
        
    def draw(self):
        """ Draw the Widget """
        self.textWindow.prepareWindow(self.cursor)
        startLine = self.textWindow.top_line
        endLine = self.textWindow.top_line + self.textWindow.window_height

        if endLine > self.textStore.numLines():
            endLine = self.textStore.numLines()
            
        maxLength = len(str(endLine - 1))
        for i in range(startLine, endLine):
            lineNumber = str(i)
            lineNumber = lineNumber.zfill(maxLength)
            line = self.textStore.getLine(i)
            if i == self.cursor.line:
                self.printCursorLine(line, lineNumber)
            else:
                self.printNormalLine(line, lineNumber)
                
    def printCursorLine(self, line, lineNumber):
        """ Prints a single line with the cursor to the console """
        startCol = self.textWindow.left_col
        endCol = self.textWindow.left_col + self.textWindow.window_width

        beforeCursor = line[startCol:self.cursor.col]
        if self.cursor.col < len(line):
            cursor = Window.terminal.reverse(line[self.cursor.col])
            afterCursor = line[self.cursor.col+1:endCol]
        else:
            cursor = Window.terminal.reverse(" ")
            afterCursor = ""
        
        self.printTextLine("{0}{1}{2}".format(beforeCursor, cursor, afterCursor), lineNumber)

    def printNormalLine(self, line, lineNumber):
        """ Prints a single line to the console """
        startCol = self.textWindow.left_col
        endCol = self.textWindow.left_col + self.textWindow.window_width

        self.printTextLine(line[startCol:endCol], lineNumber)
        
    def printTextLine(self, line, lineNumber):
        """  """
        print "{0}: {1}{t.normal}\r".format(lineNumber, line, t=Window.terminal)
        
    def getLinesToPrint(self):
        """ Returns the number of printable lines """
        numLines = self.textStore.numLines()
        if numLines > self.NUM_LINES:
            return self.NUM_LINES
        else:
            return numLines