import re

class MockFunc:
    """ Mocks a function """
    ops = ["-=", "+=", "*=", "/="]

    def __init__(self, filename, func):
        """  """
        self.vars = {}
        self.code = []

        self.filename = filename
        self.func = func

        # This version is a multi-line version.
        # self.func_regex = r'^[ \t]*def[ \t]+{function_name!s}[ \t]*\(.*(,[ \t]*\n)*.*\)[ \t]*:'.format(function_name = func)

        self.func_regex = r'^[ \t]*def[ \t]+{func_name!s}[ \t]*\(.*'.format(func_name = func)

        self.loadCode()

    def loadCode(self):
        """ Loads the code from the file """
        lines = self.loadFile()
        funcStart = self.findFunc(lines)
        
        for line in lines[funcStart+1:]:
            line = line.strip()
            
            if not line.find("+=") == -1:
                codeLine = self.cleanArgs(line)
                self.code.append(codeLine)
            elif not line.find("=") == -1:
                index = line.find("=")
                varName = line[0:index].strip()
                value = line[index+1:].strip()
                
                valueStr = self.cleanArgs(value)
                execStr = "self.vars[{0}] = {1}".format('"'+varName + '"', valueStr)
                exec(execStr)
            else:
                codeLine = self.cleanArgs(line)
                self.code.append(codeLine)
                
    def cleanArgs(self, line):
        """  Replace variables in the line with the dictionary equivalent """
        words = self.cutLine(line)
        for i in range(len(words)):
            word = words[i]
            for key in self.vars.keys():
                if word == key:
                    words[i] = 'self.vars["{0}"]'.format(key)
                    
        cleanedLine = ""
        for word in words:
            cleanedLine += word
        return cleanedLine
        
    def cutLine(self, line):
        """ Cuts a string on all separating whatchamahoosits """
        words = line.split()
        tempWords = []
        for word in words:
            tempWords.append(word)
            if not word == words[-1]:
                tempWords += [" "]
        words = tempWords
        
        for c in [".", "*", "+", "-", "=", "/", "[", "]", ","]:
            words = self.cutWord(words, c)
               
        return words
                    
    def cutWord(self, words, sep):
        """ """
        tempWords = []
        for word in words:
            splitWord = word.split(sep)
            for i in range(len(splitWord)):
                piece = splitWord[i]
                tempWords.append(piece)
                if not i == (len(splitWord)-1):
                    tempWords += [sep]
                    
        return tempWords
        

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
        print "Playing"
        print self.vars
        for line in self.code:
            print 
            print "Executing:", line
            #execStr = self.cleanArgs(line)
            exec(line)
            print self.vars
            
            
                
if __name__ == "__main__":
    m = MockFunc("test_func.py", "test_func")
    #print "\n\n\n\n\n\n"
    m.play()
