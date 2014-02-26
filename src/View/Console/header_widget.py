from kao_gui.console.console_widget import ConsoleWidget

class HeaderWidget(ConsoleWidget):
    """ Represents the view for a Editor Header """
    
    def __init__(self, editor):
        """ Initialize the view """
        self.editor = editor
        self.cursor = editor.cursor
        
    def draw(self):
        """ Draw the Widget """
        headerString = "{t.clear}Current file: {t.blue}{0}{t.normal} | Line: {1} | Col: {2}\r"
        print headerString.format(self.editor.base_filename, self.cursor.line+1, self.cursor.col+1, t=self.terminal)