from knot import apply_knot_bindings, OneWayBinding, has_scope

@has_scope
class FileController:
    """ Handles interaction with a file """
    file = OneWayBinding('file')
    
    @apply_knot_bindings
    def __init__(self, file):
        """ Initialize with the file to bind to """