from kao_console import cls

from blessings import Terminal
import os

class Screen:
    """ Represents the screen for the Text Editor """
    NUM_LINES = 20
    
    def __init__(self, parent, debug):
        self.parent = parent
        self.textStore = parent.textStore
        self.debugging = debug
        self.terminal = Terminal()
    
    def printScreen(self):
        """ Main loop for the Text Editor """
        if not self.debugging:
            cls()
            
        print "{t.clear}Current file: {0} | Line: {1} | Col: {2}\r".format(self.parent.filename, self.parent.cursor.line, self.parent.cursor.col, t=self.terminal)
        self.printText()
        
    def printText(self):
        """ Prints a section text from the file """
        startLine = self.parent.cursor.line - self.NUM_LINES/2
        if startLine < 0:
            startLine = 0
            
        endLine = startLine + self.NUM_LINES
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
                self.printTextLine(line, lineNumber)
        
    def printCursorLine(self, line, lineNumber):
        """ Prints a single line with the cursor to the console """
        beforeCursor = line[:self.parent.cursor.col]
        if self.parent.cursor.col < len(line):
            cursor = self.terminal.reverse(line[self.parent.cursor.col])
            afterCursor = line[self.parent.cursor.col+1:]
        else:
            cursor = self.terminal.reverse(" ")
            afterCursor = ""
        #print "%s: %s%s%s\r" % (lineNumber, beforeCursor, cursor, afterCursor)
        self.printTextLine("{0}{1}{2}".format(beforeCursor, cursor, afterCursor), lineNumber)
        
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