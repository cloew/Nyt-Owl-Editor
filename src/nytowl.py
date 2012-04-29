from cursor import Cursor
from input_processor import InputProcessor
from screen import Screen

from console_helper import *

class NytOwlTextEditor:
    """ The NytOwl Text Editor """
    
    def __init__(self, filename = None):
        """  """
        self.filename = filename
        
        if filename is None:
            self.text = [""]
        else:
            try:
                file = open(filename, 'r')
                self.text = file.readlines()
                file.close()
            except IOError:
                print "Unable to open file"
                
        self.cursor = Cursor()
        self.inputProcessor = InputProcessor(self)
        self.screen = Screen(self)
        
        self.running = True
        
        
        self.cmds = {UP_ARROW:self.cursorUp,
                           DOWN_ARROW:self.cursorDown,
                           LEFT_ARROW:self.cursorLeft,
                           RIGHT_ARROW:self.cursorRight,
                           CTRL_S:self.save, 
                           ESCAPE:self.exit,
                           ENDL:self.addLine,
                           TAB:self.addTab,
                           BACKSPACE:self.remove,
                           DELETE:self.delete}
        
    def run(self):
        """ Runs the program """
        while(self.running):
            self.loop()
            
    def loop(self):
        """ Main loop for the Text Editor """
        self.screen.printScreen()
        self.inputProcessor.processInput()
            
    def cursorUp(self):
        """ Moves cursor up one line """
        self.cursor.up()
        self.normalizeCol()
        
    def cursorDown(self):
        """ Moves cursor down one line """
        self.cursor.down(len(self.text))
        self.normalizeCol()
    
    def cursorLeft(self):
        """ Moves cursor left one column """
        self.cursor.left()
        
    def cursorRight(self):
        """ Moves cursor right one column """
        self.cursor.right(len(self.text[self.cursor.line]))
        
    def currentLine(self):
        """ Returns the current line """
        return self.text[self.cursor.line]
        
    def normalizeCol(self):
        """ Normalize Column """
        line = self.currentLine()
        
        if self.cursor.col > len(line):
            self.cursor.col = len(line)
                
    def addString(self, toAdd):
        """ Adds a string at the current cursor """
        line = self.currentLine()
        col = self.cursor.col
        
        self.text[self.cursor.line] = self.concatenate(line, col, col, filler = toAdd)
        
        for i in toAdd:
            self.cursorRight()
        
    def addLine(self):
        """ Adds a new line to the file """
        line = self.currentLine()
        col = self.cursor.col
        
        lineText = line[:col]
        newlineText = line[col:]
        self.text[self.cursor.line] = lineText
        
        cut = self.cursor.line+1
        self.text = self.concatenate(self.text, cut, cut, filler = [newlineText])
        self.cursorDown()
        self.cursor.col = 0
        
    def addTab(self):
        """ Adds a Tab at the current cursor location """
        self.addString(" "*4)
        
    def remove(self):
        """ Removes a character from the line """
        if self.cursor.col == 0:
            self.removeLine()
        else:
            self.removeChar()
            
    def delete(self):
        """ Deletes a character """
        line = self.currentLine()
        if self.cursor.col == len(line):
            if self.cursor.line == len(self.text) -1:
                return
        
            self.cursorDown()
            self.removeLine()
            
        else:
            self.cursorRight()
            self.removeChar()
            
    def removeChar(self):
        """ Removes a character from a line """
        line = self.text[self.cursor.line]
        col = self.cursor.col
        
        self.text[self.cursor.line] = self.concatenate(line, col-1, col)
        self.cursorLeft()
        
    def removeLine(self):
        """ Removes a line and appends the extra characters to the line above """
        if self.cursor.line == 0:
            return
        
        line = self.text[self.cursor.line]
        
        self.cursor.col = len(self.text[self.cursor.line-1])
        
        self.text[self.cursor.line-1] += line
        
        self.text = self.concatenate(self.text, self.cursor.line, self.cursor.line+1, filler = [])
        self.cursorUp()
        
    def concatenate(self, toCut, firstCut, lastCut, filler = ""):
        return toCut[:firstCut] + filler + toCut[lastCut:]
        
    def save(self):
        """  """
        if self.noFile():
            self.filename = str(raw_input("Enter filename to save to: "))
        
        try:
            file = open(self.filename, 'w')
            for line in self.text:
                file.write(line + "\n")
            file.close()
        except IOError:
            print "Unable to open file"
            
    def exit(self):
        """ Exits the game """
        self.running = False
            
    def noFile(self):
        return self.filename is None