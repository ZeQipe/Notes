class NoteModel:
    def __init__(self, title, content, color, is_task=False, deadline=None):
        self.title = title
        self.content = content
        self.color = color
        self.is_task = is_task
        self.deadline = deadline
        self.is_completed = False


class NotesStorage:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content, color, is_task, deadline):
        note = NoteModel(title, content, color, is_task, deadline)
        self.notes.append(note)

    def update_note(self, note, title, content, color, is_task, deadline):
        note.title = title
        note.content = content
        note.color = color
        note.is_task = is_task
        note.deadline = deadline

    def delete_note(self, note):
        self.notes.remove(note)

    def toggle_task_status(self, note):
        note.is_completed = not note.is_completed
