import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel
from operacoes_crud import criar_produto, listar_produtos, atualizar_produto, deletar_produto

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gerenciamento de Produtos")
        layout = QVBoxLayout()

        self.nome_input = QLineEdit()
        self.descricao_input = QLineEdit()
        self.preco_input = QLineEdit()

        layout.addWidget(QLabel("Nome do Produto"))
        layout.addWidget(self.nome_input)
        layout.addWidget(QLabel("Descrição"))
        layout.addWidget(self.descricao_input)
        layout.addWidget(QLabel("Preço"))
        layout.addWidget(self.preco_input)

        btn_criar = QPushButton("Criar Produto")
        btn_criar.clicked.connect(self.criar_produto)
        layout.addWidget(btn_criar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def criar_produto(self):
        nome = self.nome_input.text()
        descricao = self.descricao_input.text()
        preco = float(self.preco_input.text())
        criar_produto(nome, descricao, preco)

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
app.exec_()
