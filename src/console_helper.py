import sys, tty, termios
import select
import curses

ESCAPE = 27
ARROW_ESCAPE = 91
ENDL = 13
TAB = 9

BACKSPACE = 127
DELETE = 51

HOME = 72
END = 70

CTRL_S = 19
UP_ARROW = 65
DOWN_ARROW = 66
RIGHT_ARROW = 67
LEFT_ARROW = 68


KAO_UP = 260
KAO_DOWN = 261
KAO_LEFT = 262
KAO_RIGHT = 263
KAO_DELETE = 264
KAO_HOME = 265
KAO_END = 266

metaCharToKAO = {UP_ARROW:KAO_UP,
                              DOWN_ARROW:KAO_DOWN,
                              LEFT_ARROW:KAO_LEFT,
                              RIGHT_ARROW:KAO_RIGHT,
                              DELETE:KAO_DELETE,
                              HOME:KAO_HOME,
                              END:KAO_END
                             }

def getch():
    """ Retrieves a single character from the command line """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        char = ord(sys.stdin.read(1))
        metaChars = getMetaCharacters()
    finally:
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old_settings)
    return processMetaCharacter(char, metaChars)
    
def cls():
    """ Clears the console """
    sys.stdout.write("\033c")
    
def getMetaCharacters():    
        """ """
        metaBytes = []
        while True:
            metaByte = getMetaCharacter()
            if metaByte is None:
                break
            else:
                metaBytes.append(metaByte)
        return metaBytes

def getMetaCharacter():  
    """ Gets a Metadata Character """
    metaByte = None
    i,o,e = select.select([sys.stdin],[],[],0.0001)
    for s in i:
        if s == sys.stdin:
            metaByte = ord(sys.stdin.read(1))
    return metaByte
    
def processMetaCharacter(char, metaChars):
    """ Processes an escaped meta-data character """
    if char == ESCAPE and len(metaChars) > 0 and metaChars[0] == ARROW_ESCAPE:
        if metaChars[1] in metaCharToKAO:
            return metaCharToKAO[metaChars[1]]
        return ord(" ")
    return char
        