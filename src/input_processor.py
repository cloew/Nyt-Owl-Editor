from console_helper import *

import curses

class InputProcessor:
    """ Processor of command line input """
    
    def __init__(self, parent, debug):
        """ Set up the Input Processor """
        self.debugging = debug
        self.addString = parent.addString
        self.cmds = {CTRL_S:parent.save, 
                           ESCAPE:self.processEscape,
                           ENDL:parent.addLine,
                           TAB:parent.addTab,
                           BACKSPACE:parent.remove}
                           
                           
        self.escapeCmds = {ESCAPE:parent.exit,
                                     ARROW_ESCAPE:self.processArrowEscape}
                                     
        self.arrowCmds = {UP_ARROW:parent.cursorUp,
                                   DOWN_ARROW:parent.cursorDown,
                                   LEFT_ARROW:parent.cursorLeft,
                                   RIGHT_ARROW:parent.cursorRight,
                                   DELETE:parent.delete,
                                   HOME:parent.cursorStart,
                                   END:parent.cursorEnd}
        
    def processInput(self):
        """ Processes the command line input """
        c, val = self.getInput()
        
        if val in self.cmds.keys():
            self.cmds[val]()
        else:
            self.addString(c)
            
    def processEscape(self):
        """ Processes an escape sequence """
        c, val = self.getInput()
        
        if val in self.escapeCmds.keys():
            self.escapeCmds[val]()
        
    def processArrowEscape(self):
        """ Processes an Arrow Excape command """
        c, val = self.getInput()
        
        if val == DELETE:
                self.getInput()
        
        if val in self.arrowCmds.keys():
            self.arrowCmds[val]()
            
    def getInput(self):
        """ Gets a char and its ord """
        c = getch()
        val = ord(c)
        
        if self.debugging:
            print val, "\r"
        
        return c, val