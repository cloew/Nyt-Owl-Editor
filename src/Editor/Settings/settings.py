
class Settings:
    """ Represents the Settings for an open file """
    SOFT_TABS = 1
    HARD_TABS = 2
    
    def __init__(self):
        """ Initialize the Settings """
        self.tabStyle = Settings.SOFT_TABS
        self.tabSize = 4