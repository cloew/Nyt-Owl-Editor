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


ArrowEscapeToKAO = {UP_ARROW:KAO_UP,
                                  DOWN_ARROW:KAO_DOWN,
                                  LEFT_ARROW:KAO_LEFT,
                                  RIGHT_ARROW:KAO_RIGHT,
                                  DELETE:KAO_DELETE,
                                  HOME:KAO_HOME,
                                  END:KAO_END
                                 }


MetaCharToKAO = {ARROW_ESCAPE:ArrowEscapeToKAO
                             }