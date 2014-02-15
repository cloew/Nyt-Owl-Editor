from pbf.Commands import command_manager
from pbf.helpers.filename_helper import GetPythonClassnameFromFilename
from pbf.kao.nytowl.templates import TemplatesRoot
from pbf.templates import template_manager

class NewTextStoreOperation:
    """ Command to Create a new Text Store Operation """
    category = "new"
    command = "text-store-operation"
    description = "Create a new Text Store operation"
    minimumNumberOfArguments = 1
    
    def run(self, args):
        """ Run the command """
        filename = args[0]
        print "Creating Text Store Operation at:", filename
        self.createOperation(filename)
        
    def createOperation(self, filename):
        """ Create a Text Store Operation """
        classname = GetPythonClassnameFromFilename(filename)
        template_manager.CopyTemplate(filename, "text_store_operation.py", {"%ClassName%":classname}, TemplatesRoot)
    
    def help(self):
        """ Print Command usage """
        print "Usage: pbf {category} {command} [path/to/class]".format(category=self.category, command=self.command)
        print "Create a new Text Store Operation at the location given"
    
command_manager.RegisterCommand(NewTextStoreOperation)