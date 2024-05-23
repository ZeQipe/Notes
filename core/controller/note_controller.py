from core.view.note_view import NoteView


class NoteController:
    """Контроллер для управления представлением заметки."""

    def __init__(self, note):
        self.view = NoteView(note)
