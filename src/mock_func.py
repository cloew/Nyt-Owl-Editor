

class MockFunc:
    """ Mocks a function """
    
    def __init__(self, filename, func):
        """  """
        self.vars = []
        self.code = []
        
        self.filename = filename
        self.func = func
    
        self.loadCode()
    
    def loadCode(self):
        """ Loads the code from the file """
        lines = self.loadFile()
        funcStart = self.findFunc(lines)
        
        
        print "Function starts on line: %d" % funcStart

    def loadFile(self):
        try:
            file = open(self.filename, 'r')
        except IOError:
            print "Unable to open file"
            exit(-1)
            
        return file.readlines()
        
    def findFunc(self, lines):
        for i in range(len(lines)):
            line = lines[i]
            if not line.find("def "+ self.func) == -1:
                print "YATAAA!!! We found it"
                return i
                
                
if __name__ == "__main__":
    m = MockFunc("test_func.py", "test_func")
    