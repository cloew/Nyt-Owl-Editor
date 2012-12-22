from kao_console import cls
from text_window import TextWindow
from blessings import Terminal
import os

class Screen:
    """ Represents the screen for the Text Editor """
    #NUM_LINES = 20
    
    def __init__(self, parent, debug):
        self.parent = parent
        self.textStore = parent.textStore
        self.debugging = debug
        self.terminal = Terminal()
        self.textWindow = TextWindow()
    
    def printScreen(self):
        """ Main loop for the Text Editor """
        headerString = "Current file: {t.blue}{0}{t.normal} | Line: {1} | Col: {2}\r"
        if not self.debugging:
            cls()
            headerString = "{t.clear}" + headerString
            
        print headerString.format(self.parent.filename, self.parent.cursor.line, self.parent.cursor.col, t=self.terminal)
        self.printText()
        
    def printText(self):
        """ Prints a section text from the file """
        self.textWindow.prepareWindow(self.parent.cursor, self.terminal)
        startLine = self.textWindow.top_line
        endLine = self.textWindow.top_line + self.textWindow.window_height

        if endLine > self.textStore.numLines():
            endLine = self.textStore.numLines()
            
        maxLength = len(str(endLine - 1))
        for i in range(startLine, endLine):
            lineNumber = str(i)
            lineNumber = lineNumber.zfill(maxLength)
            line = self.textStore.getLine(i)
            if i == self.parent.cursor.line:
                self.printCursorLine(line, lineNumber)
            else:
                self.printNormalLine(line, lineNumber)
        
    def printCursorLine(self, line, lineNumber):
        """ Prints a single line with the cursor to the console """
        startCol = self.textWindow.left_col
        endCol = self.textWindow.left_col + self.textWindow.window_width

        beforeCursor = line[startCol:self.parent.cursor.col]
        if self.parent.cursor.col < len(line):
            cursor = self.terminal.reverse(line[self.parent.cursor.col])
            afterCursor = line[self.parent.cursor.col+1:endCol]
        else:
            cursor = self.terminal.reverse(" ")
            afterCursor = ""
        #print "%s: %s%s%s\r" % (lineNumber, beforeCursor, cursor, afterCursor)
        self.printTextLine("{0}{1}{2}".format(beforeCursor, cursor, afterCursor), lineNumber)

    def printNormalLine(self, line, lineNumber):
        """ Prints a single line to the console """
        startCol = self.textWindow.left_col
        endCol = self.textWindow.left_col + self.textWindow.window_width

        beforeCursor = line[startCol:self.parent.cursor.col]
        self.printTextLine(line[startCol:endCol], lineNumber)
        
    def printTextLine(self, line, lineNumber):
        """  """
        print "{0}: {1}{t.normal}\r".format(lineNumber, line, t=self.terminal)
        
    def getLinesToPrint(self):
        """ Returns the number of printable lines """
        numLines = self.textStore.numLines()
        if numLines > self.NUM_LINES:
            return self.NUM_LINES
        else:
            return numLines