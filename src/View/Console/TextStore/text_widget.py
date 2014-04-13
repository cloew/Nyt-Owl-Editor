from text_window import TextWindow
from Editor.Layer.layer import Layer
from View.Console.TextStore.cursor_text_line_widget import CursorTextLineWidget
from View.Console.TextStore.text_line_widget import TextLineWidget

from kao_gui.console.console_widget import ConsoleWidget

class TextWidget(ConsoleWidget):
    """ Represents the view for a Text Widget """
    
    def __init__(self, editor):
        """ Initialize the view """
        self.cursor = editor.cursor
        self.textStore = editor.textStore
        self.textWindow = editor.textWindow
        self.settings = editor.settings
        self.layer = Layer()
        
    def draw(self):
        """ Draw the Widget """
        self.textWindow.prepareWindow(self.cursor)
        startLine, endLine = self.getStartAndEndLines()
            
        lineWidgets = self.getLineWidgets(startLine, endLine)
            
        for lineWidget in  lineWidgets:
            lineWidget.draw()
            
        self.drawLayer()
            
    def getStartAndEndLines(self):
        """ Return the Proper Start and End Lines """
        startLine = self.textWindow.top_line
        endLine = self.textWindow.bottom_line

        if endLine > self.textStore.numLines():
            endLine = self.textStore.numLines()
            
        return startLine, endLine
        
    def getLineWidgets(self, startLine, endLine):
        """ Return all the Line Widgets """
        lineWidgets = []
        for i in range(startLine, endLine):
            line = self.textStore.getLine(i)
            lineNumber = self.getLineNumberString(endLine, i+1)
            if i == self.cursor.line:
                widget = CursorTextLineWidget(line, lineNumber, self.textWindow, self.settings, self.cursor)
            else:
                widget = TextLineWidget(line, lineNumber, self.textWindow, self.settings)
            lineWidgets.append(widget)
            
        return lineWidgets
        
    def getLineNumberString(self, endLine, index):
        """ Return the Line Number String """
        maxLength = len(str(endLine))
        lineNumber = str(index)
        return lineNumber.zfill(maxLength)
        
    def drawLayer(self):
        """ Draw the current layer """
        lines = self.layer.generateLines(self.cursor, self.textStore, self.textWindow)
        if len(lines) > 0:
            lines = ['|'+str(line) for line in lines]
            maxLineLength = max([len(line) for line in lines])
            self.drawAtPosition(lines, (self.terminal.width-maxLineLength, 2))