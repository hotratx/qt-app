import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        self.lista_arquivos = QListWidget(self)

        # Adiciona um item à lista
        item = QListWidgetItem(f"Erro no arquivo: aa")
        self.lista_arquivos.addItem(item)

        # Define a cor do texto para toda a QListWidget usando QSS
        self.lista_arquivos.setStyleSheet("QListWidget { color: red; }")

        layout.addWidget(self.lista_arquivos)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('QListWidget com Cor Personalizada')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
