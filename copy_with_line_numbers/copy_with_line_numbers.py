import sublime, sublime_plugin
import os

class CopyWithLineNumbersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = sublime.Window.active_view(sublime.active_window())
        sels = self.view.sel()

        settings = sublime.load_settings("copy_with_line_numbers.sublime-settings")
        relative_path = settings.get("copy_relative_filepath", False)
        # set file name
        if view.file_name():
            filename = view.file_name()
            if view.window().folders() and relative_path:
                # Use relative file name
                folders = view.window().folders()
                for folder in folders:
                    if folder in filename:
                        filename = filename.replace(folder, '')
                        break
            output = "File: " + filename + "\n"
        else:
            output = "File: <unsaved>\n"

        # To print all the line numbers with the same lenght
        max_line_num = self.get_line_num(sels[-1].end())
        max_line_num_len = len(str(max_line_num))
        format_string = "%0" + str(max_line_num_len) + "d: %s\n"

        # handle text
        isFollowupSelection = None
        for selection in sels:
            if isFollowupSelection:
            	# split multi selections with ---
            	output += "---\n"
            else:
            	# but not the first one
            	isFollowupSelection = True
            # for each selection
            selection = self.view.line(selection)  # Extend selection to full lines
            first_line_num = self.get_line_num(selection.begin())
            lines = self.view.substr(selection).split("\n")  # Considers all line breaks
            for i, line in enumerate(lines):
                output += format_string % (first_line_num + i, line)

        # send to clipboard
        sublime.set_clipboard(output)

    def get_line_num(self, point):
        return self.view.rowcol(point)[0] + 1