
import sublime, sublime_plugin

class MyDemonstrationCommand(sublime_plugin.TextCommand):
#
	def run(self, edit):
	#
		print("MyDemonstrationCommand is running. Let's add some parenthesis around %d selection(s)" % len(self.view.sel()));
		for region in self.view.sel():
		#
			selectedText = self.view.substr(region);
			self.view.replace(edit, region, "(" + selectedText + ")");
		#
	#
#

class MyDemonstrationEventListener(sublime_plugin.EventListener):
#
	def on_query_completions(self, view, prefix, locations):
	#
		result = [];
		result.append(["MyDemoReplacement", "This is the replacement text"]);
		result.append(["MyAwesomeReplacement", "We can put whatever we want here. Awesome!"]);
		return result;
	#
#