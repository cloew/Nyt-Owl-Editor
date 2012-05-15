import re

class MockFunc:
    """ Mocks a function """

    def __init__(self, filename, func):
        """  """
        self.vars = {}
        self.code = []

        self.filename = filename
        self.func = func

        # self.func_regex = r'^[ \t]*def[ \t]+{function_name!s}[ \t]*\(.*(,[ \t]*\n)*.*\)[ \t]*:'.format(function_name = func)

        self.func_regex = r'^[ \t]*def[ \t]+{func_name!s}[ \t]*\(.*'.format(func_name = func)

        self.loadCode()

    def loadCode(self):
        """ Loads the code from the file """
        lines = self.loadFile()
        funcStart = self.findFunc(lines)
        
        for line in lines[funcStart+1:]:
            line = line.strip()
            print line
            
            if not line.find("+=") == -1:
                self.code.append(line)
            elif not line.find("=") == -1:
                index = line.find("=")
                varName = line[0:index].strip()
                value = line[index+1:].strip()
                execStr = "self.vars[{0}]".format('"'+varName + '"') + "=" + value
                exec(execStr)
                print value
            

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
            matchObj = re.match(self.func_regex, line)
            if matchObj:
                return i
                
    def play(self):
        """ Plays the code """
        print self.vars
        for line in self.code:
            opIndex = line.find("+=")
            varName = line[0:opIndex].strip()
            value = line[opIndex+2:]
            execStr = "self.vars[{0}]".format('"'+varName + '"') + "+=" + value
            exec(execStr)
            print self.vars
            
            
                
if __name__ == "__main__":
    m = MockFunc("test_func.py", "test_func")
    print "\n\n\n\n\n\n"
    m.play()
