from kao_console.ascii import *

from string import printable

def GetCursorCommands(editor):
    """ Return the Cursor Commands """
    return {KAO_UP:editor.cursorUp,
            KAO_DOWN:editor.cursorDown,
            KAO_LEFT:editor.cursorLeft,
            KAO_RIGHT:editor.cursorRight,
            KAO_HOME:editor.cursorStart,
            KAO_END:editor.cursorEnd,
            KAO_PAGE_UP:editor.cursorPageUp,
            KAO_PAGE_DOWN:editor.cursorPageDown,
            KAO_CTRL_HOME:editor.cursorStartOfFile,
            KAO_CTRL_END:editor.cursorEndOfFile,
            KAO_CTRL_RIGHT:editor.cursorNextWord}