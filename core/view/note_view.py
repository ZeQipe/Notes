from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QCheckBox, QRadioButton,
                               QFrame, QMessageBox)
from PySide6.QtCore import Qt

class NoteView(QWidget):
    def __init__(self, note, view_mode, main_controller):
        super().__init__()
        self.note = note
        self.view_mode = view_mode
        self.main_controller = main_controller
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Заголовок заметки
        title = QLabel(self.note['title'])
        layout.addWidget(title)

        # Визуальная разделительная линия
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("background-color: black; min-height: 2px; max-height: 2px;")
        layout.addWidget(line)

        # Тело заметки
        body = QLabel(self.note['body'])
        layout.addWidget(body)

        # Кнопки "Изменить" и "Удалить"
        buttons_layout = QHBoxLayout()
        edit_button = QPushButton("Изменить")
        edit_button.clicked.connect(self.edit_note)
        delete_button = QPushButton("Удалить")
        delete_button.clicked.connect(self.delete_note)
        buttons_layout.addWidget(edit_button)
        buttons_layout.addWidget(delete_button)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

    def edit_note(self):
        self.main_controller.edit_note_editor(self.note)

    def delete_note(self):
        confirmation = QMessageBox.question(self, "Удалить заметку", "Вы уверены, что хотите удалить эту заметку?", QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.Yes:
            self.main_controller.delete_note_editor(self.note)
