from console_helper import *

import curses.ascii

class InputProcessor:
    """ Processor of command line input """
    
    def __init__(self, parent, debug):
        """ Set up the Input Processor """
        self.debugging = debug
        self.addString = parent.addString
        self.cmds = {CTRL_S:parent.save, 
                           ESCAPE:parent.exit,#self.processEscape,
                           ENDL:parent.addLine,
                           TAB:parent.addTab,
                           BACKSPACE:parent.remove,
                           KAO_UP:parent.cursorUp,
                           KAO_DOWN:parent.cursorDown,
                           KAO_LEFT:parent.cursorLeft,
                           KAO_RIGHT:parent.cursorRight,
                           KAO_DELETE:parent.delete,
                           KAO_HOME:parent.cursorStart,
                           KAO_END:parent.cursorEnd}
        
    def processInput(self):
        """ Processes the command line input """
        val = self.getInput()
        
        if val in self.cmds.keys():
            self.cmds[val]()
        elif curses.ascii.isprint(val):
            self.addString(chr(val))
            
    def getInput(self):
        """ Gets a char and its ord """
        val = getch()
        
        if self.debugging:
            print val, "\r"
        
        return val