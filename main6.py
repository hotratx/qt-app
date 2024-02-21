import os
import xmltodict
from qt_material import apply_stylesheet
from multiprocessing import Pool, cpu_count, current_process
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


class Error:
    def __init__(self, file: str):
        self.file = file


def read_xml(name):
    if name == "/home/hotratx/repos/handler-xml/061116/105/nfce_v_0611161051000430559.xml":
        return Error(name)
    with open(name, 'r', encoding='utf-8') as arquivo:
        xml_dict = xmltodict.parse(arquivo.read())
    return xml_dict


def save_mongo(file): print(f"save file: {file}")


class SeletorDePastaApp(QWidget):
    def __init__(self):
        super().__init__()
        # Botão para selecionar a pasta
        self.button_select_folder = QPushButton("Selecione a pasta")
        self.button_select_folder.clicked.connect(self.show_dialog_folder)

        self.list_errors = QListWidget()

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setFormat("%p%")  # Adiciona a porcentagem

        layout = QVBoxLayout(self)
        layout.addWidget(self.button_select_folder)
        layout.addWidget(self.list_errors)
        layout.addWidget(self.progress_bar)

    def show_dialog_folder(self):
        select_folder = QFileDialog.getExistingDirectory(self, "Selecione uma pasta")
        
        if select_folder:
            print(f"pasta selecionada: {select_folder}")
            list_path = list()
            list_path = listar_pastas_e_subpastas(select_folder, list_path)
            # Limpar a lista de arquivos
            self.list_errors.clear()
            print(f"Quantidade de arquivos: {len(list_path)}")
            self.list_errors.addItem(f"Foram encontrados {len(list_path)} arquivos .xml")
            self.run(list_path)

    def run(self, path):
        self.progress_bar.setRange(0, len(path))
        self.progress_bar.setValue(0)

        np = cpu_count()
        print(f"cpu_count: {np}")
        output = []
        pool = Pool(processes=np)
        results = [pool.apply_async(read_xml, args=(file,)) for file in path]

        for i, p in enumerate(results):
            self.progress_bar.setValue(i)
            QApplication.processEvents()
            resp = p.get()
            if isinstance(resp, Error):
                print(f"achou error: {resp}")
                self.list_errors.addItem(f"Erro no arquivo: {resp.file}")
            output.append(resp)
        print("terminou")
        print(f"result len: {len(output)}")


def main():
    app = QApplication([])
    apply_stylesheet(app, theme='light_blue.xml')

    janela = SeletorDePastaApp()
    janela.show()

    app.exec()

if __name__ == "__main__":
    main()
