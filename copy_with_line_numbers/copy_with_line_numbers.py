import sublime, sublime_plugin
import os

class CopyWithLineNumbersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = sublime.Window.active_view(sublime.active_window())

        # set file name
        if view.file_name():
        	output = "File: " + view.file_name() + "\n"
        else:
        	output = "File: <unsaved>\n"

        # handle text
        isFollowupSelection = None
        for selection in view.sel():
            if isFollowupSelection:
            	# split multi selections with ---
            	output += "---\n"
            else:
            	# but not the first one
            	isFollowupSelection = True
            # for each selection
            for line in view.lines(selection):
                output += str(view.rowcol(line.begin())[0] + 1) + ": " + view.substr(line) + "\n"

        # send to clipboard
        sublime.set_clipboard(output)