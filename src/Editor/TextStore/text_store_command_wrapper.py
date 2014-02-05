
class TextStoreCommandWrapper:
    """ Wrapper for Text Store Commands """
    
    def __init__(self, parent):
        """ Initialize the Cursor Command Wrapper with its parent """
        self.cursor = parent.cursor
        self.textStore = parent.textStore
        self.addCommandsToParent(parent)
        
    def addCommandsToParent(self, parent):
        """ Add commands to the parent """
        commands = ["addString", "addLine", "addTab", "remove",
                    "delete"]
        
        for command in commands:
            setattr(parent, command, getattr(self, command))
        
    def currentLine(self):
        """ Returns the current line """
        return self.textStore.text[self.cursor.line]
                
    def addString(self, toAdd):
        """ Adds a string at the current cursor """
        line = self.currentLine()
        col = self.cursor.col
        
        self.textStore.text[self.cursor.line] = self.concatenate(line, col, col, filler = toAdd)
        
        for i in toAdd:
            self.cursor.right()
        
    def addLine(self, event=None):
        """ Adds a new line to the file """
        line = self.currentLine()
        col = self.cursor.col
        
        lineText = line[:col]
        newlineText = line[col:]
        self.textStore.text[self.cursor.line] = lineText
        
        cut = self.cursor.line+1
        self.textStore.text = self.concatenate(self.textStore.text, cut, cut, filler = [newlineText])
        self.cursor.down()
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
        
            self.cursor.down()
            self.removeLine()
            
        else:
            self.cursor.right()
            self.removeChar()
            
    def removeChar(self):
        """ Removes a character from a line """
        line = self.textStore.text[self.cursor.line]
        col = self.cursor.col
        
        self.textStore.text[self.cursor.line] = self.concatenate(line, col-1, col)
        self.cursor.left()
        
    def removeLine(self):
        """ Removes a line and appends the extra characters to the line above """
        if self.cursor.line == 0:
            return
        
        line = self.textStore.text[self.cursor.line]
        
        self.cursor.col = len(self.textStore.text[self.cursor.line-1])
        
        self.textStore.text[self.cursor.line-1] += line
        
        self.textStore.text = self.concatenate(self.textStore.text, self.cursor.line, self.cursor.line+1, filler = [])
        self.cursor.up()
        
    def concatenate(self, toCut, firstCut, lastCut, filler = ""):
        return toCut[:firstCut] + filler + toCut[lastCut:]