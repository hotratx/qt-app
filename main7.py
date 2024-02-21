import os
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QListWidget, QListWidgetItem, QProgressBar, QGridLayout
from PySide6.QtCore import Qt

class SeletorDePastaApp(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        layout_principal = QVBoxLayout(self)
        
        # Layout de grade para organizar os widgets
        layout_grid = QGridLayout()

        # Botão para selecionar a pasta
        self.botao_selecionar_pasta = QPushButton("Selecione a pasta")
        self.botao_selecionar_pasta.clicked.connect(self.exibir_dialogo_selecao_pasta)
        layout_grid.addWidget(self.botao_selecionar_pasta, 0, 0, 1, 2)

        # Lista para mostrar os arquivos
        self.lista_arquivos = QListWidget()
        layout_grid.addWidget(self.lista_arquivos, 1, 0, 1, 2)

        # Barra de progresso
        self.barra_progresso = QProgressBar(self)
        layout_grid.addWidget(self.barra_progresso, 2, 0, 1, 2)

        # Adicionar o layout de grade ao layout principal
        layout_principal.addLayout(layout_grid)

    def exibir_dialogo_selecao_pasta(self):
        pasta_selecionada = QFileDialog.getExistingDirectory(self, "Selecione uma pasta")
        
        if pasta_selecionada:
            # Limpar a lista de arquivos
            self.lista_arquivos.clear()

            # Listar os arquivos na pasta
            arquivos = os.listdir(pasta_selecionada)

            # Configurar a barra de progresso
            self.barra_progresso.setRange(0, len(arquivos))
            self.barra_progresso.setValue(0)

            # Adicionar os arquivos na lista
            for i, arquivo in enumerate(arquivos):
                item = QListWidgetItem(arquivo)
                self.lista_arquivos.addItem(item)

                # Atualizar a barra de progresso
                self.barra_progresso.setValue(i + 1)
                QApplication.processEvents()  # Garantir que a interface do usuário seja atualizada

def main():
    app = QApplication([])

    janela = SeletorDePastaApp()
    janela.show()

    app.exec()

if __name__ == "__main__":
    main()
