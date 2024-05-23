from PySide6.QtWidgets import QMessageBox, QDialog
from core.view.main_view import MainView
from core.view.note_editor import NoteEditor

class MainController:
    """Контроллер главного окна приложения."""

    def __init__(self):
        self.view = MainView(self)
        self.view.create_note_button.clicked.connect(self.open_note_editor)

    def open_note_editor(self):
        """Открывает окно для создания новой заметки."""
        editor = NoteEditor(parent=self.view)
        if editor.exec() == QDialog.Accepted:
            note_data = editor.get_note_data()
            self.view.notes.append(note_data)
            self.view.update_notes()

    def edit_note_editor(self, note):
        """Открывает окно для редактирования существующей заметки."""
        editor = NoteEditor(note, parent=self.view)
        if editor.exec() == QDialog.Accepted:
            note_data = editor.get_note_data()
            index = self.view.notes.index(note)
            self.view.notes[index] = note_data
            self.view.update_notes()

    def delete_note_editor(self, note):
        """Удаляет существующую заметку."""
        self.view.notes.remove(note)
        self.view.update_notes()
