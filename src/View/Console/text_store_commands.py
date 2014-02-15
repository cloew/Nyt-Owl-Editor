from kao_console.ascii import *

from string import printable

def GetTextStoreCommands(editor):
    """ Return the Text Store Commands """
    commands = {}
    for character in printable:
        commands[character] = editor.addString
        
    commands.update({CTRL_S:editor.save,
                     ENDL:editor.addLine,
                     TAB:editor.addTab,
                     BACKSPACE:editor.remove,
                     KAO_DELETE:editor.delete,
                     KAO_SHIFT_TAB:editor.removeTab,
                     CTRL_Z:editor.undo,
                     CTRL_Y:editor.redo})
                
    return commands