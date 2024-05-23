from core.model.note import Note


class ListNoteItem:
    """Класс для элементов списка в заметке типа 'Список'."""

    def __init__(self, text, completed=False):
        self.text = text
        self.completed = completed

    def toggle(self):
        """Метод для переключения статуса выполнения элемента списка."""
        self.completed = not self.completed


class ListNote(Note):
    """Класс для заметок типа 'Список'."""

    def __init__(self, title, body, color, items=None):
        super().__init__(title, body, color)
        self.items = items if items else []

    def edit(self, title=None, body=None, color=None):
        """Метод для редактирования заметки типа 'Список'."""
        super().edit(title, body, color)

    def toggle_item(self, index):
        """Метод для переключения статуса выполнения элемента списка по индексу."""
        if 0 <= index < len(self.items):
            self.items[index].toggle()
