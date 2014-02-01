from nytowl import NytOwlTextEditor
from nytowl_screen import NytowlScreen

from View.Console.TextStore.text_window import TextWindow

from kao_console.ascii import *
from kao_gui.console.console_controller import ConsoleController

class NytowlController(ConsoleController):
    """ Controller for the Nyt Owl Text Editor """
    
    def __init__(self, filename):
        """ Initialize the Nyt Owl Text Editor Controller """
        textWindow = TextWindow()
        self.editor = NytOwlTextEditor(filename, textWindow)
        
        commands = {CTRL_S:self.editor.save,
                     ENDL:self.editor.addLine,
                     TAB:self.editor.addTab,
                     BACKSPACE:self.editor.remove,
                     KAO_UP:self.editor.cursorUp,
                     KAO_DOWN:self.editor.cursorDown,
                     KAO_LEFT:self.editor.cursorLeft,
                     KAO_RIGHT:self.editor.cursorRight,
                     KAO_DELETE:self.editor.delete,
                     KAO_HOME:self.editor.cursorStart,
                     KAO_END:self.editor.cursorEnd,
                     KAO_PAGE_UP:self.editor.cursorPageUp,
                     KAO_PAGE_DOWN:self.editor.cursorPageDown}
        
        screen = NytowlScreen(self.editor)
        ConsoleController.__init__(self, screen, commands=commands)