from core.model.note import Note
from core.model.task_note import TaskNote
from core.model.list_note import ListNote


class NoteBuilder:
    """Класс для построения заметок различных типов."""

    def __init__(self):
        self.title = ''
        self.body = ''
        self.color = ''
        self.deadline = None
        self.items = []

    def set_title(self, title):
        """Метод для установки заголовка заметки."""
        self.title = title
        return self

    def set_body(self, body):
        """Метод для установки тела заметки."""
        self.body = body
        return self

    def set_color(self, color):
        """Метод для установки цвета заметки."""
        self.color = color
        return self

    def set_deadline(self, deadline):
        """Метод для установки дедлайна заметки (для заметок типа 'Задача')."""
        self.deadline = deadline
        return self

    def set_items(self, items):
        """Метод для установки элементов списка заметки (для заметок типа 'Список')."""
        self.items = items
        return self

    def build(self, note_type='note'):
        """Метод для построения заметки заданного типа."""
        if note_type == 'task':
            return TaskNote(self.title, self.body, self.color, self.deadline)
        elif note_type == 'list':
            return ListNote(self.title, self.body, self.color, self.items)
        else:
            return Note(self.title, self.body, self.color)
