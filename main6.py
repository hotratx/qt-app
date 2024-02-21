import os
import xmltodict
import dask.bag as db
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QListWidget, QListWidgetItem, QProgressBar
from PySide6.QtCore import Qt


def listar_pastas_e_subpastas(caminho, data_list):
    for nome in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, nome)
        if os.path.isdir(caminho_completo):
            listar_pastas_e_subpastas(caminho_completo, data_list)
        if caminho_completo.endswith(".xml"):
            data_list.append(caminho_completo)
    return data_list


def read_xml(name):
    with open(name, 'r', encoding='utf-8') as arquivo:
        xml_dict = xmltodict.parse(arquivo.read())
    return xml_dict


def save_mongo(file):
    print(f"save file: {file}")


def run_dask(list_path):
    dados = db.from_sequence(list_path).map(read_xml)
    result = dados.compute()
    return result

# data_list = list()
# list_path = listar_pastas_e_subpastas("./061116/", data_list)
# print(f"tamanho da lista de path: {len(list_path)}")


class SeletorDePastaApp(QWidget):
    def __init__(self):
        super().__init__()

        # Layout principal
        layout = QVBoxLayout(self)

        # Botão para selecionar a pasta
        self.botao_selecionar_pasta = QPushButton("Selecione a pasta")
        self.botao_selecionar_pasta.clicked.connect(self.exibir_dialogo_selecao_pasta)
        layout.addWidget(self.botao_selecionar_pasta)

        # Barra de progresso
        self.barra_progresso = QProgressBar(self)
        layout.addWidget(self.barra_progresso)

        # Lista para mostrar os arquivos
        self.lista_arquivos = QListWidget()
        layout.addWidget(self.lista_arquivos)

    def exibir_dialogo_selecao_pasta(self):
        pasta_selecionada = QFileDialog.getExistingDirectory(self, "Selecione uma pasta")
        
        if pasta_selecionada:
            # Limpar a lista de arquivos
            print(f"pasta selecionada: {pasta_selecionada}")
            list_path = list()
            listar_pastas_e_subpastas(pasta_selecionada, list_path)
            self.lista_arquivos.clear()
            print(f"Quantidade de arquivos: {len(list_path)}")
            result = run_dask(list_path, )
            print(f"resultado do run_dask: {result}")

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
