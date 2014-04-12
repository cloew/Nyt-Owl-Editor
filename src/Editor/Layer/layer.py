from kao_pyrunner.FunctionFinder.python_function_finder import PythonFunctionFinder
from kao_pyrunner.Runner.python_runner import PythonRunner

class Layer:
    """ Represents a layer """
    
    def __init__(self):
        """ Initialize the layer """
        self.lines = []
        
    def generateLines(self, cursor, textStore, textWindow):
        """ Generate the layer lines for the cursor, text store and current text window """
        currentFunctionLines = PythonFunctionFinder().findFunction(textStore.text, cursor.line, cursor.col)
        try:
            results = PythonRunner(currentFunctionLines).processFunction()
            return [str(results[key]) for key in results]
        except Exception as error: # Want to catch any excpetion that happens in the Python Runner
            return [str(error)]