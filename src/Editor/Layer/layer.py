from kao_pyrunner.FunctionFinder import PythonFunctionFinder
from kao_pyrunner.Runner import PythonRunner

class Layer:
    """ Represents a layer """
    
    def __init__(self):
        """ Initialize the layer """
        self.lines = []
        
    def generateLines(self, cursor, textStore, textWindow):
        """ Generate the layer lines for the cursor, text store and current text window """
        currentFunctionLines = PythonFunctionFinder().findFunction(testStore.text, cursor.line, cursor.col)
        results = PythonRunner(currentFunctionLines).processFunction()
        return results