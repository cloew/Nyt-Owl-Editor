import sys, tty, termios
import select
import curses

from kao_console_constants import *

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
    dict = MetaCharToKAO
    if char == ESCAPE and len(metaChars) > 0 and metaChars[0] == ARROW_ESCAPE:
        for metaChar in metaChars:
            if metaChar in dict:
                dict = dict[metaChar]
                if type(dict) is int:
                    return dict
            else:
                return ord(" ")
    return char
        