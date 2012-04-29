import sys, tty, termios

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

def getch():
    """ Retrieves a single character from the command line """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old_settings)
    return ch
    
def cls():
    """ Clears the console """
    sys.stdout.write("\033c")