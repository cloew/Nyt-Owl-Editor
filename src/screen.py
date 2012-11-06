from console_helper import cls

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
            
        print "Current file: %s | Line: %d | Col: %d\r" % (self.parent.filename, self.parent.cursor.line, self.parent.cursor.col)
            
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
                self.printLine(line, lineNumber)
            
    def printLine(self, line, lineNumber):
        """ Prints a single line to the console """
        print "%s: %s\r" % (lineNumber, line)
        
    def printCursorLine(self, line, lineNumber):
        """ Prints a single line with the cursor to the console """
        beforeCursor = line[:self.parent.cursor.col]
        if self.parent.cursor.col < len(line):
            cursor = self.terminal.reverse(line[self.parent.cursor.col])
            afterCursor = line[self.parent.cursor.col+1:]
        else:
            cursor = self.terminal.reverse(" ")
            afterCursor = ""
        print "%s: %s%s%s\r" % (lineNumber, beforeCursor, cursor, afterCursor)
        
    def getLinesToPrint(self):
        """ Returns the number of printable lines """
        numLines = self.textStore.numLines()
        if numLines > self.NUM_LINES:
            return self.NUM_LINES
        else:
            return numLines