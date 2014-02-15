
class ActionListManager:
    """ Manages the list of actions to handle performing undos and redos """
    
    def __init__(self):
        """ Initialize the Action List Manager """
        self.actionList = []
        self.nextActionIndex = 0
        
    def addAction(self, action):
        """ Add an action to the action list """
        self.actionList[self.nextActionIndex:] = [action]
        self.nextActionIndex += 1
        
    def undoPreviousAction(self):
        """ Undo the previous action """
        if self.nextActionIndex > 0:
            self.nextActionIndex -= 1
            action = self.actionList[self.nextActionIndex]
            action.undo()
            
    def redoPreviousAction(self):
        """ Redo the previous undone action """
        if self.nextActionIndex < len(self.actionList):
            action = self.actionList[self.nextActionIndex]
            action.do()
            self.nextActionIndex += 1