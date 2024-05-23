from core.view.note_editor import NoteEditor


class NoteEditorController:
    """Контроллер для управления окном создания и редактирования заметок."""

    def __init__(self):
        self.view = NoteEditor()
