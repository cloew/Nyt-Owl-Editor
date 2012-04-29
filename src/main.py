from nytram import NytRamTextEditor

import sys

def main(args):
    """   """
    if len(args) > 0:
        n = NytRamTextEditor(filename = args[0])
    else:
        n = NytRamTextEditor()
        
    n.run()
    
    
if __name__ == "__main__":
    main(sys.argv[1:])