import sublime, sublimeplugin

from mock_func import MockFunc

# This simple plugin will add 'Hello, World!' to the end of the buffer when run.
# To run it, save it within the User/ directory, then open the console (Ctrl+~),
# and type: view.runCommand('sample')
#
# See http://www.sublimetext.com/docs/plugin-basics for more information
class SampleCommand(sublimeplugin.Plugin):
	def onModified(self, view):
		""" Run on modified """
		print "Modified"
		lines = view.substr(sublime.Region(0, view.size())).split("\n")
		self.mock = MockFunc("test_func", lines=lines)
		self.mock.play()

	def onLoad(self, view):
		""" Run on Load """
		print "Load"
		self.mock = MockFunc("test_func.py", "test_func")
