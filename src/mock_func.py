

class MockFunc:
    """ Mocks a function """
    
    def __init__(self, filename, func):
        """  """
        self.vars = {}
        self.code = []
        
        self.filename = filename
        self.func = func
    
        self.loadCode()
        
        print self.vars
        print self.code
    
    def loadCode(self):
        """ Loads the code from the file """
        lines = self.loadFile()
        funcStart = self.findFunc(lines)
        print "Function starts on line: %d" % funcStart
        
        for line in lines[funcStart+1:]:
            line = line.strip()
            print line
            
            if not line.find("+=") == -1:
                print "Adding to the variable"
                self.code.append(line)
            elif not line.find("=") == -1:
                print "Variable Assignment"
                index = line.find("=")
                varName = line[0:index].strip()
                value = int(line[index+1:].strip())
                self.vars[varName] = value
                setattr(self, varName, value)
                print "Assigning var {0}: {1}".format(varName, value)
                print self.vars[varName]
            

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
                
    def play(self):
        """ Plays the code """
        print self.vars
        for line in self.code:
            opIndex = line.find("+=")
            varName = line[0:opIndex].strip()
            value = line[opIndex+2:]
            
            evalString = str(self.vars[varName])+"+"+str(value)
            self.vars[varName] = eval(evalString)
            print self.vars
            
            
                
if __name__ == "__main__":
    m = MockFunc("test_func.py", "test_func")
    print "\n\n\n\n\n\n"
    m.play()