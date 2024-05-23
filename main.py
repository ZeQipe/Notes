import sys
from PySide6.QtWidgets import QApplication
from core.controller.main_controller import MainController


def main():
    app = QApplication(sys.argv)
    controller = MainController()
    controller.view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
