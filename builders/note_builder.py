from models.note_model import NoteModel


class NoteBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.note = NoteModel("", "", "lightyellow")

    def set_title(self, title):
        self.note.title = title
        return self

    def set_content(self, content):
        self.note.content = content
        return self

    def set_color(self, color):
        self.note.color = color
        return self

    def set_task(self, is_task):
        self.note.is_task = is_task
        return self

    def set_deadline(self, deadline):
        self.note.deadline = deadline
        return self

    def get_result(self):
        return self.note


class NoteDirector:
    def __init__(self, builder):
        self._builder = builder

    def construct(self, title, content, color, is_task, deadline):
        self._builder.reset()
        self._builder.set_title(title).set_content(content).set_color(color).set_task(is_task).set_deadline(deadline)
        return self._builder.get_result()
