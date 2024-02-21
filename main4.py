from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QApplication, QPushButton

class MeuObjeto(QObject):
    # Definindo um sinal personalizado
    meu_sinal = Signal(str)

    def __init__(self):
        super().__init__()

    @Slot()
    def slot_quando_botao_clicado(self):
        print("Botão foi clicado!")
        # Emitir o sinal com uma mensagem
        self.meu_sinal.emit("Botão clicado!")

def main():
    app = QApplication([])

    # Criar instâncias do objeto
    meu_objeto = MeuObjeto()

    # Criar um botão
    botao = QPushButton("Clique-me")

    # Conectar o clique do botão ao slot personalizado
    botao.clicked.connect(meu_objeto.slot_quando_botao_clicado)

    # Conectar o sinal personalizado ao slot personalizado
    meu_objeto.meu_sinal.connect(lambda mensagem: print(f"Recebido: {mensagem}"))

    # Exibir a aplicação
    botao.show()
    app.exec()

if __name__ == "__main__":
    main()
