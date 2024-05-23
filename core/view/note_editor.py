from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QComboBox, QDialogButtonBox

class NoteEditor(QDialog):
    def __init__(self, note=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Редактирование заметки" if note else "Создание заметки")
        self.note = note

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.title_edit = QLineEdit(note['title'] if note else '')
        self.layout.addWidget(QLabel("Заголовок"))
        self.layout.addWidget(self.title_edit)

        self.body_edit = QTextEdit(note['body'] if note else '')
        self.layout.addWidget(QLabel("Тело заметки"))
        self.layout.addWidget(self.body_edit)

        self.type_combo = QComboBox()
        self.type_combo.addItems(['text', 'task', 'list'])
        self.type_combo.setCurrentText(note['type'] if note else 'text')
        self.layout.addWidget(QLabel("Тип заметки"))
        self.layout.addWidget(self.type_combo)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

    def get_note_data(self):
        return {
            'title': self.title_edit.text(),
            'body': self.body_edit.toPlainText(),
            'type': self.type_combo.currentText(),
            'items': []
        }
