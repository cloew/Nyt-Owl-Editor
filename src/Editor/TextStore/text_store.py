

class TextStore:
    """ A class to wrap the Text Data in the file """
    
    def __init__(self, filename):
        """ Build text data from a file """
        self.text = [""]
        
        if not filename is None:
            try:
                file = open(filename, 'r')
                self.text = []
                for line in file.readlines():
                    self.text.append(line.rstrip('\n'))
                if len(self.text) == 0:
                    self.text = [""]
                file.close()
            except IOError:
                print("Unable to open file")
                
    def getLine(self, i):
        """ Returns the line i """
        return self.text[i]
        
    def numLines(self):
        """ Returns the number of lines in the text """
        return len(self.text)
                
    def lastLine(self):
        """ Returns the last valid line # """
        return len(self.text)-1
        
    def lastColumn(self, line):
        """ Returns the last valid column # in the line given """
        return len(self.text[line])