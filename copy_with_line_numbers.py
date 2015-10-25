import sublime
import sublime_plugin

class CopyWithLineNumbersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = sublime.Window.active_view(sublime.active_window())
        selections = view.sel()
        fileName = view.file_name()

        # Settings
        settings = sublime.load_settings("CopyWithLineNumbersReloaded.sublime-settings")
        relativeFilePath = settings.get("copy_relative_filepath", False)

        # Set file name
        if fileName:
            folders = view.window().folders()
            if folders and relativeFilePath:
                fileName = self.removeAbsolutePath(fileName, folders)
            outputFileName = fileName
        else:
            outputFileName = "<unsaved>"

        output = "File: " + outputFileName + "\n"

        # To print all the line numbers with the same length
        largestLineNumber = self.getLineNumber(selections[-1].end())
        largestLineNumberLength = len(str(largestLineNumber))
        outputLineFormatString = "%0" + str(largestLineNumberLength) + "d: %s\n"

        # handle text
        isFollowupSelection = None
        for selection in selections:
            if isFollowupSelection:
                # split multi selections with ---
                output += "---\n"
            else:
                # but not the first one
                isFollowupSelection = True
            # for each selection
            selection = view.line(selection)  # Extend selection to full line
            firstLineNumberInSelection = self.getLineNumber(selection.begin())
            linesInSelection = view.substr(selection).split("\n")  # Considers all line breaks
            for i, line in enumerate(linesInSelection):
                output += outputLineFormatString % (firstLineNumberInSelection + i, line)

        # Send to clipboard
        sublime.set_clipboard(output)

    def getLineNumber(self, point):
        return self.view.rowcol(point)[0] + 1

    def removeAbsolutePath(self, fileName, folderList):
        for folder in folderList:
            if folder in fileName:
                fileName = fileName.replace(folder, '')
            break
        return fileName
