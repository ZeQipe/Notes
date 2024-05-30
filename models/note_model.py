from datetime import datetime

from utils.caretaker import Caretaker


class NoteModel:
    def __init__(self, title, content, color, is_task=False, deadline=None, is_completed=False):
        self.title = title
        self.content = content
        self.color = color
        self.is_task = is_task
        self.deadline = deadline
        self.is_completed = is_completed

    def to_dict(self):
        return {
            'title': self.title,
            'content': self.content,
            'color': self.color,
            'is_task': self.is_task,
            'deadline': self.deadline.isoformat() if self.deadline else None,
            'is_completed': self.is_completed,
        }

    @classmethod
    def from_dict(cls, note_dict):
        deadline = note_dict.get('deadline')
        return cls(
            title=note_dict['title'],
            content=note_dict['content'],
            color=note_dict['color'],
            is_task=note_dict['is_task'],
            deadline=datetime.fromisoformat(deadline) if deadline else None,
            is_completed=note_dict.get('is_completed', False)
        )

class NotesStorage:
    def __init__(self):
        self.caretaker = Caretaker()
        self.notes = self.caretaker.load_notes()

    def add_note(self, title, content, color, is_task, deadline):
        new_note = NoteModel(title, content, color, is_task, deadline)
        self.notes.append(new_note)
        self.caretaker.save_notes(self.notes)

    def update_note(self, note, title, content, color, is_task, deadline):
        note.title = title
        note.content = content
        note.color = color
        note.is_task = is_task
        note.deadline = deadline
        self.caretaker.save_notes(self.notes)

    def delete_note(self, note):
        self.notes.remove(note)
        self.caretaker.save_notes(self.notes)

    def toggle_task_status(self, note):
        note.is_completed = not note.is_completed
        self.caretaker.save_notes(self.notes)
