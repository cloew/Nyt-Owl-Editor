from View.Console.header_widget import HeaderWidget
from View.Console.TextStore.text_widget import TextWidget

from kao_gui.console.console_widget import ConsoleWidget

class NytowlScreen(ConsoleWidget):
    """ Represents the view for the Nyt Owl Text Editor """
    
    def __init__(self, editor):
        """ Initialize the view """
        self.headerWidget = HeaderWidget(editor)
        self.textWidget = TextWidget(editor)
        
    def draw(self):
        """ Draw the Widget """
        self.headerWidget.draw()
        self.textWidget.draw()