from nytowl import NytOwlTextEditor
from nytowl_screen import NytowlScreen

from View.Console.TextStore.text_window import TextWindow

from kao_gui.console.console_controller import ConsoleController

class NytowlController(ConsoleController):
    """ Controller for the Nyt Owl Text Editor """
    
    def __init__(self, filename):
        """ Initialize the Nyt Owl Text Editor Controller """
        textWindow = TextWindow()
        self.editor = NytOwlTextEditor(filename, textWindow)
        
        screen = NytowlScreen(self.editor)
        ConsoleController.__init__(self, screen)