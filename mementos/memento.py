import json
import os


class Memento:
    def __init__(self, filepath="notes.json"):
        self.filepath = filepath

    def save(self, notes):
        with open(self.filepath, "w") as file:
            json.dump([note.__dict__ for note in notes], file)

    def load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as file:
                data = json.load(file)
                return [NoteModel(**note_data) for note_data in data]
        return []

