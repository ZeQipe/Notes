from models.note_model import NotesStorage
from views.main_view import MainView


class MainController:
    def __init__(self):
        self.model = NotesStorage()
        self.view = MainView()
        self.view.set_controller(self)

    def add_note(self, title, content, color, is_task, deadline):
        self.model.add_note(title, content, color, is_task, deadline)
        self.view.update_notes(self.model.notes)

    def update_note(self, note, title, content, color, is_task, deadline):
        self.model.update_note(note, title, content, color, is_task, deadline)
        self.view.update_notes(self.model.notes)

    def delete_note(self, note):
        self.model.delete_note(note)
        self.view.update_notes(self.model.notes)

    def toggle_task_status(self, note):
        self.model.toggle_task_status(note)
        self.view.update_notes(self.model.notes)
