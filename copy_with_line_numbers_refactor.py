import sublime
import sublime_plugin


class Section(object):
    __slots__ = (
        'startLineNumber',
        'lines'
    )

class Selection(object):
    __slots__ = (
        'largest_line_number_length',
        'folders',
        'sections',
        'fileName'
    )


def createOutput(selections: Selection) -> str:
    output = selections.fileName + ":\n" if selections.fileName is not None else '<unsaved>'

    output += "\n".join(selections.sections[0].lines)

    for selection in selections.sections[1:]:
        output += "\n---\n"
        for lineIndexInSelection, line in enumerate(selection.lines):
            output += "%d: %s\n" % (selection.startLineNumber + lineIndexInSelection, line)

    return output


class CopyWithLineNumbersRefactorCommand(sublime_plugin.TextCommand):
    def file_name(self) -> str:
        return self.view.file_name()

    def folders(self) -> list:
        return self.view.window().folders()

    def set_clipboard(self, content: str) -> None:
        sublime.set_clipboard(content)

    def get_line_number(self, point) -> int:
        return self.view.rowcol(point)[0] + 1

    def largest_line_number_length(self) -> int:
        largestLineNumber = self.get_line_number(self.view.sel()[-1].end())
        return len(str(largestLineNumber))

    def selections(self) -> Selection:
        selections = self.view.sel()

        result = Selection()
        result.largest_line_number_length = self.largest_line_number_length()
        result.folders = self.folders()
        result.sections = list()
        result.fileName = self.file_name()

        for selection in selections:
            selection = self.view.line(selection)

            section = Section()
            section.startLineNumber = self.get_line_number(selection.begin())
            section.lines = self.view.substr(selection).split("\n")

            result.sections.append(section)

        return result


    def run(self, edit) -> None:
        sublime.status_message(str('ok'))
        self.set_clipboard(str(createOutput(self.selections())))
