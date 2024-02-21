import sys
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QProgressBar

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setFormat("%p%")  # Adiciona a porcentagem

        self.start_button = QPushButton('Iniciar', self)
        self.start_button.clicked.connect(self.start_progress)

        layout = QVBoxLayout(self)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.start_button)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.progress_value = 0

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Barra de Progresso com Porcentagem')
        self.show()

    def start_progress(self):
        self.progress_value = 0
        self.progress_bar.setValue(0)
        self.timer.start(100)  # Atualiza a cada 100 milissegundos

    def update_progress(self):
        self.progress_value += 1
        self.progress_bar.setValue(self.progress_value)

        if self.progress_value == 100:
            self.timer.stop()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
