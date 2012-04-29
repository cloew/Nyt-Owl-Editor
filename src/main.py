from nytowl import NytOwlTextEditor

import sys

def main(args):
    """   """
    if len(args) > 0:
        n = NytOwlTextEditor(filename = args[0])
    else:
        n = NytOwlTextEditor()
        
    n.run()
    
    
if __name__ == "__main__":
    main(sys.argv[1:])