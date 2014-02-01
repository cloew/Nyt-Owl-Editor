from kao_console.ascii import *

from string import printable

def GetTextStoreCommands(editor):
    """ Return the Text Stores """
    commands = {}
    for character in printable:
        commands[character] = editor.addString
        
    commands.update({CTRL_S:editor.save,
                     ENDL:editor.addLine,
                     TAB:editor.addTab,
                     BACKSPACE:editor.remove,
                     KAO_DELETE:editor.delete})
                
    return commands