from controllers.main_controller import MainController

if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    controller = MainController()
    controller.view.show()
    sys.exit(app.exec())
