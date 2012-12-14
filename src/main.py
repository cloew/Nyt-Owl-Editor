from nytowl import NytOwlTextEditor

import sys


def processArgs(args):
    """ Processes the arguments passed on the command line """
    filename = None
    debug = False
    
    for i in range(len(args)):
        cmd = args[i]
        if cmd == "-d":
            debug = True
        else:
            filename = cmd

    return filename, debug
    
def main(args):
    """   """
    filename, debug = processArgs(args)
    n = NytOwlTextEditor(filename, debug)
    n.run()
    
    
if __name__ == "__main__":
    main(sys.argv[1:])