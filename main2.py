from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Layout principal
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Botão para abrir o diálogo de arquivo
        button = QPushButton("Selecione uma pasta", self)
        button.clicked.connect(self.show_file_dialog)
        layout.addWidget(button)

    def show_file_dialog(self):
        options = QFileDialog.Options()
        folder_path = QFileDialog.getExistingDirectory(None, "Selecione uma pasta", options=options)

        if folder_path:
            print(f"Você selecionou a pasta: {folder_path}")


if __name__ == "__main__":
    app = QApplication([])
    main_window = MyMainWindow()
    main_window.show()
    app.exec()
