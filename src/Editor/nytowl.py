from Editor.Cursor.cursor import Cursor
from Editor.Cursor.cursor_command_wrapper import CursorCommandWrapper
from Editor.TextStore.text_store import TextStore

import os

class NytOwlTextEditor:
    """ The NytOwl Text Editor """
    
    def __init__(self, filename, textWindow):
        """  """
        self.filename = filename
        self.textWindow = textWindow
        
        self.textStore = TextStore(filename)
        self.cursor = Cursor(self.textStore)
        
        self.cursorCommandWrapper = CursorCommandWrapper(self) 
        
    def currentLine(self):
        """ Returns the current line """
        return self.textStore.text[self.cursor.line]
                
    def addString(self, toAdd):
        """ Adds a string at the current cursor """
        line = self.currentLine()
        col = self.cursor.col
        
        self.textStore.text[self.cursor.line] = self.concatenate(line, col, col, filler = toAdd)
        
        for i in toAdd:
            self.cursorRight()
        
    def addLine(self, event=None):
        """ Adds a new line to the file """
        line = self.currentLine()
        col = self.cursor.col
        
        lineText = line[:col]
        newlineText = line[col:]
        self.textStore.text[self.cursor.line] = lineText
        
        cut = self.cursor.line+1
        self.textStore.text = self.concatenate(self.textStore.text, cut, cut, filler = [newlineText])
        self.cursorDown()
        self.cursor.col = 0
        
    def addTab(self, event=None):
        """ Adds a Tab at the current cursor location """
        self.addString(" "*4)
        
    def remove(self, event=None):
        """ Removes a character from the line """
        if self.cursor.col == 0:
            self.removeLine()
        else:
            self.removeChar()
            
    def delete(self, event=None):
        """ Deletes a character """
        line = self.currentLine()
        if self.cursor.col == len(line):
            if self.cursor.line == len(self.textStore.text) -1:
                return
        
            self.cursorDown()
            self.removeLine()
            
        else:
            self.cursorRight()
            self.removeChar()
            
    def removeChar(self):
        """ Removes a character from a line """
        line = self.textStore.text[self.cursor.line]
        col = self.cursor.col
        
        self.textStore.text[self.cursor.line] = self.concatenate(line, col-1, col)
        self.cursorLeft()
        
    def removeLine(self):
        """ Removes a line and appends the extra characters to the line above """
        if self.cursor.line == 0:
            return
        
        line = self.textStore.text[self.cursor.line]
        
        self.cursor.col = len(self.textStore.text[self.cursor.line-1])
        
        self.textStore.text[self.cursor.line-1] += line
        
        self.textStore.text = self.concatenate(self.textStore.text, self.cursor.line, self.cursor.line+1, filler = [])
        self.cursorUp()
        
    def concatenate(self, toCut, firstCut, lastCut, filler = ""):
        return toCut[:firstCut] + filler + toCut[lastCut:]
        
    def save(self, event=None):
        """  """
        if self.noFile():
            self.filename = str(raw_input("Enter filename to save to: "))
        
        try:
            file = open(self.filename, 'w')
            for line in self.textStore.text:
                file.write(line + "\n")
            file.close()
        except IOError:
            print "Unable to open file"
            
    def noFile(self):
        return self.filename is None

    @property
    def base_filename(self):
        """ Return the File's basename """
        if self.filename is None:
            return None
        else:
            return os.path.basename(self.filename)