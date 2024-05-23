from PySide6.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QFrame, QScrollArea, QLabel
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from .compact_note_view import CompactNoteView
from .expanded_note_view import ExpandedNoteView

class MainView(QMainWindow):
    """Главное окно приложения."""

    def __init__(self, main_controller):
        super().__init__()
        self.main_controller = main_controller
        self.setWindowTitle("Заметки")

        # Устанавливаем статичный размер окна
        self.setFixedSize(800, 600)

        # Создаем центральный виджет и основной макет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout()
        central_widget.setLayout(self.main_layout)

        # Создаем кнопку "Создать заметку"
        self.create_note_button = QPushButton("Создать")
        self.create_note_button.setFixedSize(100, 40)
        self.create_note_button.clicked.connect(self.create_note)

        # Создаем кнопку для переключения вида заметок
        self.switch_view_button = QPushButton()
        self.switch_view_button.setIcon(QIcon("path/to/icon.png"))
        self.switch_view_button.setToolTip("Сменить вид")
        self.switch_view_button.setFixedSize(40, 40)
        self.switch_view_button.clicked.connect(self.switch_view)

        # Создаем верхний макет и добавляем в него кнопки
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.create_note_button)
        top_layout.addStretch()
        top_layout.addWidget(self.switch_view_button, alignment=Qt.AlignRight)

        # Добавляем верхний макет в основной макет
        self.main_layout.addLayout(top_layout)

        # Создаем черную линию
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("background-color: black; min-height: 2px; max-height: 2px;")
        self.main_layout.addWidget(line)

        # Создаем область для заметок
        self.notes_area = QScrollArea()
        self.notes_area.setWidgetResizable(True)
        self.notes_container = QWidget()
        self.notes_layout = QVBoxLayout()
        self.notes_container.setLayout(self.notes_layout)
        self.notes_area.setWidget(self.notes_container)
        self.main_layout.addWidget(self.notes_area)

        self.notes = []
        self.view_mode = 'compact'

        # Изначально отображаем сообщение, что заметок нет
        self.no_notes_label = QLabel("Заметок нету, создайте первую заметку")
        self.no_notes_label.setAlignment(Qt.AlignCenter)
        self.notes_layout.addWidget(self.no_notes_label)

    def create_note(self):
        """Метод для создания новой заметки"""
        self.main_controller.open_note_editor()

    def switch_view(self):
        """Метод для переключения вида заметок"""
        self.view_mode = 'expanded' if self.view_mode == 'compact' else 'compact'
        self.update_notes()

    def update_notes(self):
        """Метод для обновления списка заметок"""
        # Удаляем все виджеты из макета
        for i in reversed(range(self.notes_layout.count())):
            widget = self.notes_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        if not self.notes:
            self.notes_layout.addWidget(self.no_notes_label)
        else:
            for note in self.notes:
                if self.view_mode == 'compact':
                    note_view = CompactNoteView(note, self.main_controller)
                else:
                    note_view = ExpandedNoteView(note, self.main_controller)
                self.notes_layout.addWidget(note_view)
