import sys, tty, termios
from cursor import Cursor

ESCAPE = 27
ARROW_ESCAPE = 91
ENDL = 13
TAB = 9

BACKSPACE = 127
DELETE = 51

HOME = 72
END = 70

CTRL_S = 19
UP_ARROW = 65
DOWN_ARROW = 66
RIGHT_ARROW = 67
LEFT_ARROW = 68

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old_settings)
    return ch

class NytRamTextEditor:
    """ The NytRam Text Editor """
    
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
        print "\r"
        print "Current file: %s | Line: %d | Col: %d\r" % (self.filename, self.cursor.line, self.cursor.col)
        c, val = self.getInput()
        
        if val == ESCAPE:
            c, val = self.getInput()
            if val == ARROW_ESCAPE:
                c, val = self.getInput()
                if val == DELETE:
                    self.getInput()
        
        if val in self.cmds.keys():
            self.cmds[val]()
        else:
            self.addChar(c)
            
        print self.currentLine(), "\r"
        
    def getInput(self):
        """ Gets a char and its ord """
        c = getch()
        print ord(c), "\r"
        val = ord(c)
        return c, val
            
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
        
        first = line[:col]
        last = line[col:]
        
        self.text[self.cursor.line] = first + toAdd + last
        
        for i in toAdd:
            self.cursorRight()
        
    def addChar(self, c):
        """ Adds a char at the current cursor position """
        line = self.text[self.cursor.line]
        col = self.cursor.col
        
        first = line[:col]
        last = line[col:]
        self.text[self.cursor.line] = first + c + last
        self.cursorRight()
        
    def addLine(self):
        """ Adds a new line to the file """
        line = self.currentLine()
        col = self.cursor.col
        
        lineText = line[:col]
        newlineText = line[col:]
        self.text[self.cursor.line] = lineText
        
        first = self.text[:self.cursor.line+1]
        last = self.text[self.cursor.line+1:]
        
        self.text = first + [newlineText] + last
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
        
        first = line[:col-1]
        last = line[col:]
        self.text[self.cursor.line] = first + last
        self.cursorLeft()
        
    def removeLine(self):
        """ Removes a line and appends the extra characters to the line above """
        if self.cursor.line == 0:
            return
        
        line = self.text[self.cursor.line]
        
        self.cursor.col = len(self.text[self.cursor.line-1])
        
        self.text[self.cursor.line-1] += line
        
        first = self.text[:self.cursor.line]
        last = self.text[self.cursor.line+1:]
        
        self.text = first + last
        self.cursorUp()
        
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