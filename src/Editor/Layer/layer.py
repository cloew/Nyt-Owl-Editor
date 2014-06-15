from kao_pyrunner.FunctionFinder.python_function_finder import PythonFunctionFinder
from kao_pyrunner.Runner.invalid_function_exception import InvalidFunctionException
from kao_pyrunner.Runner.python_runner import PythonRunner

class Layer:
    """ Represents a layer """
    
    def __init__(self):
        """ Initialize the layer """
        self.lines = []
        
    def generateLines(self, cursor, textStore, textWindow):
        """ Generate the layer lines for the cursor, text store and current text window """
        functionStartAndStop = PythonFunctionFinder().findFunction(textStore.text, cursor.line, cursor.col)
        cleanedResults = []
        
        if functionStartAndStop is not None:
            try:
                results = PythonRunner(textStore.text, functionStartAndStop).processFunction()
                cleanedResults = [str(results[key]) for key in results]
            except InvalidFunctionException:
                pass
        return cleanedResults