from knot import apply_knot_bindings, OneWayBinding, has_scope

@has_scope
class LineController:
    """ Handles control for a particular line in the file """
    index = OneWayBinding('index')
    line = OneWayBinding('line')
    
    @apply_knot_bindings
    def __init__(self, index, line):
        """ Initialize the Line Controller with the line to wrap and the index of the line """
        
    @property
    def lineNumber(self):
        """ Return the line number for this line """
        return self.index + 1