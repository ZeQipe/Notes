from core.model.note import Note


class TaskNote(Note):
    """Класс для заметок типа 'Задача'."""

    def __init__(self, title, body, color, deadline):
        super().__init__(title, body, color)
        self.deadline = deadline

    def edit(self, title=None, body=None, color=None, deadline=None):
        """Метод для редактирования заметки типа 'Задача'."""
        super().edit(title, body, color)
        if deadline:
            self.deadline = deadline
