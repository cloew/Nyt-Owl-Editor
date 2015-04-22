from Editor.nytowl import NytOwlTextEditor

from knot import KnotService

class NytOwlEditor:
    """ Service for interacting with the open files """
    args = KnotService("cli-args")
    
    def __init__(self):
        """ Initialize the editor """
        filenames = self.args[1:]
        filename = filenames[0] if len(filenames) > 0 else None
        self.file = NytOwlTextEditor(filename, None)
        print(filename)