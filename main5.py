import os
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QListWidget, QListWidgetItem

class SeletorDePastaApp(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        layout = QVBoxLayout(self)

        # Botão para selecionar a pasta
        self.botao_selecionar_pasta = QPushButton("Selecione a pasta")
        self.botao_selecionar_pasta.clicked.connect(self.exibir_dialogo_selecao_pasta)
        layout.addWidget(self.botao_selecionar_pasta)

        # Lista para mostrar os arquivos
        self.lista_arquivos = QListWidget()
        layout.addWidget(self.lista_arquivos)

    def exibir_dialogo_selecao_pasta(self):
        pasta_selecionada = QFileDialog.getExistingDirectory(self, "Selecione uma pasta")
        
        if pasta_selecionada:
            # Limpar a lista de arquivos
            self.lista_arquivos.clear()

            # Adicionar os arquivos na lista
            for arquivo in os.listdir(pasta_selecionada):
                item = QListWidgetItem(arquivo)
                self.lista_arquivos.addItem(item)

def main():
    app = QApplication([])

    janela = SeletorDePastaApp()
    janela.show()

    app.exec()

if __name__ == "__main__":
    main()

