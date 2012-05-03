from console_helper import cls

import os

class Screen:
    """ Represents the screen for the Text Editor """
    NUM_LINES = 20
    
    def __init__(self, parent, debug):
        self.parent = parent
        self.debugging = debug
    
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
        if endLine >= len(self.parent.text):
            endLine = len(self.parent.text)
            
        maxLength = len(str(endLine - 1))
        for i in range(startLine, endLine):
            lineNumber = str(i)
            lineNumber = lineNumber.zfill(maxLength)
            line = self.parent.text[i]
            print "%s: %s\r" % (lineNumber, line)
        
    def getLinesToPrint(self):
        """ Returns the number of printable lines """
        numLines = len(self.parent.text)
        if numLines > self.NUM_LINES:
            return self.NUM_LINES
        else:
            return numLines