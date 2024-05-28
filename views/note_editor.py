from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLineEdit, QTextEdit, QHBoxLayout, QPushButton, QLabel,
    QComboBox, QColorDialog, QDateTimeEdit
)
from PySide6.QtCore import QDateTime, Qt
from datetime import datetime


class NoteEditor(QDialog):
    def __init__(self, controller, note=None):
        super().__init__()
        self.controller = controller
        self.note = note
        self.setWindowTitle("Редактирование заметки" if note else "Создание заметки")
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()

        self.title_edit = QLineEdit(self.note.title if self.note else "")
        self.title_edit.setPlaceholderText("Наименование заметки (макс 30 символов)")
        self.title_edit.setMaxLength(30)
        layout.addWidget(self.title_edit)

        self.type_combo = QComboBox()
        self.type_combo.addItems(["Текстовая", "Задача", "Список"])
        self.type_combo.currentTextChanged.connect(self.on_type_change)
        layout.addWidget(self.type_combo)

        self.note_type_label = QLabel("Примечание: пункты списка будут разделены по переносам строки.")
        self.note_type_label.setWordWrap(True)
        self.note_type_label.hide()
        layout.addWidget(self.note_type_label)

        self.content_edit = QTextEdit(self.note.content if self.note else "")
        self.content_edit.setStyleSheet("background-color: lightyellow;")
        layout.addWidget(self.content_edit)

        self.color_button = QPushButton("Выбрать цвет")
        self.color_button.clicked.connect(self.select_color)
        layout.addWidget(self.color_button)

        self.deadline_edit = QDateTimeEdit()
        self.deadline_edit.setDateTime(QDateTime.currentDateTime())
        self.deadline_edit.setCalendarPopup(True)
        self.deadline_edit.hide()
        layout.addWidget(self.deadline_edit)

        if self.note:
            if self.note.is_task:
                self.type_combo.setCurrentText("Задача")
                self.deadline_edit.setDateTime(QDateTime(self.note.deadline) if self.note.deadline else QDateTime.currentDateTime())
            elif '\n' in self.note.content:
                self.type_combo.setCurrentText("Список")
                self.note_type_label.show()
            else:
                self.type_combo.setCurrentText("Текстовая")

        buttons_layout = QHBoxLayout()
        save_button = QPushButton("Сохранить")
        save_button.clicked.connect(self.save_note)
        buttons_layout.addWidget(save_button)
        cancel_button = QPushButton("Отмена")
        cancel_button.clicked.connect(self.close)
        buttons_layout.addWidget(cancel_button)
        layout.addLayout(buttons_layout)

        self.setLayout(layout)

    def select_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.selected_color = color.name()
            self.content_edit.setStyleSheet(f"background-color: {self.selected_color};")

    def on_type_change(self, note_type):
        if note_type == "Список":
            self.note_type_label.show()
            self.color_button.show()
            self.deadline_edit.hide()
        elif note_type == "Задача":
            self.note_type_label.hide()
            self.color_button.hide()
            self.deadline_edit.show()
        else:
            self.note_type_label.hide()
            self.color_button.show()
            self.deadline_edit.hide()

    def save_note(self):
        title = self.title_edit.text()
        content = self.content_edit.toPlainText()
        color = self.selected_color if hasattr(self, 'selected_color') else self.note.color if self.note else 'lightyellow'
        note_type = self.type_combo.currentText()
        is_task = (note_type == "Задача")
        deadline = self.deadline_edit.dateTime().toPython() if is_task else None

        if self.note:
            self.controller.update_note(self.note, title, content, color, is_task, deadline)
        else:
            self.controller.add_note(title, content, color, is_task, deadline)
        self.close()
