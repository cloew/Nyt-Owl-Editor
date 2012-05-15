import re

class MockFunc:
    """ Mocks a function """

    def __init__(self, filename, func):
        """  """
        self.vars = []
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
            matchObj = re.match(self.func_regex, line)
            if matchObj:
                print "YATAAA!!! We found it"
                return i


if __name__ == "__main__":
    m = MockFunc("test_func.py", "test_func")
