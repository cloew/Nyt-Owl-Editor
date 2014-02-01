from cursor import Cursor
from text_store import TextStore

class NytOwlTextEditor:
    """ The NytOwl Text Editor """
    
    def __init__(self, filename, textWindow):
        """  """
        self.filename = filename
        self.textWindow = textWindow
        
        self.textStore = TextStore(filename)
        self.cursor = Cursor(self.textStore)
            
    def cursorUp(self, event=None):
        """ Moves cursor up one line """
        self.cursor.up()
        
    def cursorDown(self, event=None):
        """ Moves cursor down one line """
        self.cursor.down()
    
    def cursorLeft(self, event=None):
        """ Moves cursor left one column """
        self.cursor.left()
        
    def cursorRight(self, event=None):
        """ Moves cursor right one column """
        self.cursor.right()
        
    def cursorStart(self, event=None):
        """ Move cursor to the start of the line """
        self.cursor.toStartOfLine()
        
    def cursorEnd(self, event=None):
        """ Move cursor to the end of the line """
        self.cursor.toEndOfLine()

    def cursorPageUp(self, event=None):
        """ Move the cursor up a page """
        self.cursor.jumpUp(self.textWindow.window_height)
        self.textWindow.top_line = self.cursor.line

    def cursorPageDown(self, event=None):
        """ Move the cursor down a page """
        self.cursor.jumpDown(self.textWindow.window_height)
        self.textWindow.top_line = self.cursor.line
        
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
            
    def exit(self):
        """ Exits the game """
        self.running = False
            
    def noFile(self):
        return self.filename is None
