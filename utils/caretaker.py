import os
import json
from pathlib import Path


class Caretaker:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.filepath = self._get_save_path()

    def _get_save_path(self):
        local_app_data = os.getenv('LOCALAPPDATA')
        save_dir = os.path.join(local_app_data, 'ZeNotes')
        os.makedirs(save_dir, exist_ok=True)
        return os.path.join(save_dir, self.filename)

    def save_notes(self, notes):
        with open(self.filepath, 'w') as f:
            json_notes = [note.to_dict() for note in notes]
            json.dump(json_notes, f, indent=4)

    def load_notes(self):
        from models.note_model import NoteModel

        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, 'r') as f:
                json_notes = json.load(f)
                return [NoteModel.from_dict(note) for note in json_notes]
        except (json.JSONDecodeError, IOError):
            return []
