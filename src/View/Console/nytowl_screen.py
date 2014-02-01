from View.Console.TextStore.text_widget import TextWidget

from kao_gui.console.console_widget import ConsoleWidget
from kao_gui.console.window import Window

class NytowlScreen(ConsoleWidget):
    """ Represents the view for the Nyt Owl Text Editor """
    
    def __init__(self, filename, textStore, cursor):
        """ Initialize the view """
        self.filename = filename
        self.cursor = cursor
        self.textWidget = TextWidget(textStore, cursor)
        
    def draw(self):
        """ Draw the Widget """
        headerString = "{t.clear}Current file: {t.blue}{0}{t.normal} | Line: {1} | Col: {2}\r"
        print headerString.format(self.filename, self.cursor.line, self.cursor.col, t=Window.terminal)
        
        self.textWidget.draw()