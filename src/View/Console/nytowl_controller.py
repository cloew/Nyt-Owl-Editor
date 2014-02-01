from nytowl_screen import NytowlScreen

from cursor import Cursor
from text_store import TextStore

from kao_gui.console.console_controller import ConsoleController

class NytowlController(ConsoleController):
    """ Controller for the Nyt Owl Text Editor """
    
    def __init__(self, filename):
        """ Initialize the Nyt Owl Text Editor Controller """
        self.filename = filename
        self.textStore = TextStore(filename)
        self.cursor = Cursor(self.textStore)
        
        screen = NytowlScreen(self.filename, self.textStore, self.cursor)
        ConsoleController.__init__(self, screen)