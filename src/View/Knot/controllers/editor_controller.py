from knot import KnotService, has_scope

@has_scope
class EditorController:
    """ Handles interaction with the Editor """
    editor = KnotService('editor')
    
    @property
    def currentFile(self):
        """ Return the current file for the editor """
        return self.editor.file