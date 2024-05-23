from core.model.memento import Memento


class Note:
    """Базовый класс для всех типов заметок."""

    def __init__(self, title, body, color):
        self.title = title
        self.body = body
        self.color = color

    def edit(self, title=None, body=None, color=None):
        """Метод для редактирования заметки."""
        if title:
            self.title = title
        if body:
            self.body = body
        if color:
            self.color = color

    def create_memento(self):
        """Метод для создания моменто (снимка состояния заметки)."""
        return Memento(self.title, self.body, self.color)

    def restore_from_memento(self, memento):
        """Метод для восстановления состояния заметки из моменто."""
        self.title = memento.title
        self.body = memento.body
        self.color = memento.color
