from kao_gui.console.window import Window

class TextWindow:
    """ Represents the widnow of the text file that is visible """

    def __init__(self):
        """ Builds the Text Window """
        self.top_line = 0
        self.left_col = 0
        self.window_height = 0
        self.window_width = 0
       
    @property
    def bottom_line(self):
        """ Return the bottom Line of the text window """
        return self.top_line + self.window_height
        
    @property
    def right_col(self):
        """ Return the right column of the text window """
        return self.left_col + self.window_width

    def prepareWindow(self, cursor):
        """ Prepares the window with the current cursor and terminal size """
        self.window_height = Window.terminal.height - 2
        self.window_width = Window.terminal.width - 2 - len(str(max(right_col, cursor.col)))
        self.checkCursorLocation(cursor)

    def checkCursorLocation(self, cursor):
        """ Check if the cursor is out of the window """
        self.checkCursorRow(cursor)
        self.checkCursorColumn(cursor)

    def checkCursorRow(self, cursor):
        """ Check if the cursor is in a row outside of the window """
        if cursor.line < self.top_line:
            self.top_line = cursor.line
        elif cursor.line >= self.bottom_line:
            self.top_line = cursor.line-self.window_height + 1 # Not sure if this is right

    def checkCursorColumn(self, cursor):
        """ Check if the cursor is in a column outside of the window """
        if cursor.col < self.left_col:
            self.left_col = cursor.col
        elif cursor.col >= self.right_col:
            self.left_col = cursor.col-self.window_width + 1 # Not sure if this is right # May need magic to deal offset from the line number