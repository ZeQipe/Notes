from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QListWidget,
    QListWidgetItem, QLabel, QHBoxLayout, QGridLayout, QCheckBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Заметки")
        self.setGeometry(100, 100, 800, 600)

        self.current_style = "compact"

        self.create_note_button = QPushButton("Создать заметку")
        self.create_note_button.clicked.connect(self.open_note_editor)

        self.toggle_style_button = QPushButton("Сменить стиль")
        self.toggle_style_button.clicked.connect(self.toggle_style)

        self.notes_widget = QWidget()
        self.no_notes_label = QLabel("Заметки отсутствуют, создайте первую!")
        self.no_notes_label.setAlignment(Qt.AlignCenter)

        self.notes_layout = QVBoxLayout()
        self.notes_layout.addWidget(self.no_notes_label)
        self.notes_widget.setLayout(self.notes_layout)

        central_widget = QWidget()
        layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.create_note_button)
        button_layout.addWidget(self.toggle_style_button)
        layout.addLayout(button_layout)
        layout.addWidget(self.notes_widget)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.detailed_view = None

        self.show()

    def set_controller(self, controller):
        self.controller = controller

    def update_notes(self, notes):
        while self.notes_layout.count() > 1:
            child = self.notes_layout.takeAt(1)
            if child.widget():
                child.widget().deleteLater()

        if not notes:
            self.no_notes_label.show()
        else:
            self.no_notes_label.hide()
            if self.current_style == "compact":
                self.show_compact_view(notes)
            else:
                self.show_detailed_view(notes)

    def show_compact_view(self, notes):
        if hasattr(self, 'detailed_view') and self.detailed_view:
            self.detailed_view.setParent(None)
            self.detailed_view = None

        self.notes_list = QListWidget()
        for note in notes:
            item_widget = QWidget()
            item_layout = QHBoxLayout()

            if note.is_task:
                checkbox = QCheckBox()
                checkbox.setChecked(note.is_completed)
                checkbox.stateChanged.connect(lambda state, note=note: self.controller.toggle_task_status(note))
                item_layout.addWidget(checkbox)

            title_label = QLabel(note.title)
            title_label.setStyleSheet(f"background-color: {note.color}; margin-left: 5px;")
            if note.is_completed:
                title_label.setStyleSheet(f"background-color: {note.color}; text-decoration: line-through; margin-left: 5px;")

            edit_button = QPushButton("Редактировать")
            edit_button.clicked.connect(lambda checked, note=note: self.open_note_editor(note))

            delete_button = QPushButton("Удалить")
            delete_button.clicked.connect(lambda checked, note=note: self.controller.delete_note(note))

            item_layout.addWidget(title_label)
            item_layout.addWidget(edit_button)
            item_layout.addWidget(delete_button)

            item_widget.setLayout(item_layout)
            item = QListWidgetItem()
            item.setSizeHint(item_widget.sizeHint())
            self.notes_list.addItem(item)
            self.notes_list.setItemWidget(item, item_widget)

        self.notes_layout.addWidget(self.notes_list)

    def show_detailed_view(self, notes):
        if hasattr(self, 'notes_list') and self.notes_list:
            self.notes_list.setParent(None)
            self.notes_list = None

        grid_layout = QGridLayout()
        row, col = 0, 0
        for note in notes:
            note_widget = QWidget()
            note_layout = QVBoxLayout()

            header_layout = QHBoxLayout()
            if note.is_task:
                checkbox = QCheckBox()
                checkbox.setChecked(note.is_completed)
                checkbox.stateChanged.connect(lambda state, note=note: self.controller.toggle_task_status(note))
                header_layout.addWidget(checkbox)
            header_label = QLabel(note.title)
            header_label.setStyleSheet("background-color: lightgrey; font-weight: bold;")
            header_layout.addWidget(header_label)
            note_layout.addLayout(header_layout)

            body_label = QLabel(note.content[:100] + "..." if len(note.content) > 100 else note.content)
            body_label.setStyleSheet(f"background-color: {note.color};")
            note_layout.addWidget(body_label)

            buttons_layout = QHBoxLayout()
            edit_button = QPushButton("Редактировать")
            edit_button.clicked.connect(lambda checked, note=note: self.open_note_editor(note))
            delete_button = QPushButton("Удалить")
            delete_button.clicked.connect(lambda checked, note=note: self.controller.delete_note(note))
            buttons_layout.addWidget(edit_button)
            buttons_layout.addWidget(delete_button)
            note_layout.addLayout(buttons_layout)

            note_widget.setLayout(note_layout)
            note_widget.setFixedSize(200, 200)
            grid_layout.addWidget(note_widget, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1

        self.detailed_view = QWidget()
        self.detailed_view.setLayout(grid_layout)
        self.notes_layout.addWidget(self.detailed_view)

    def open_note_editor(self, note=None):
        from views.note_editor import NoteEditor
        editor = NoteEditor(self.controller, note)
        editor.exec_()

    def toggle_style(self):
        self.current_style = "detailed" if self.current_style == "compact" else "compact"
        self.update_notes(self.controller.model.notes)
