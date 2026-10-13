from PyQt5 import QtCore, QtGui, QtWidgets
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from models import Base, Cliente, Animal, Consulta  # Importa os modelos definidos em models.py
from datetime import datetime

# Configuração do banco de dados
DATABASE_URL = "sqlite:///clinica_veterinaria.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Layout principal
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)

        # Títulos e Labels
        self.title_label = QtWidgets.QLabel("Operações de Álgebra Relacional", self.centralwidget)
        self.title_label.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        self.gridLayout.addWidget(self.title_label, 0, 0, 1, 2)

        # Botões de Operações
        self.projecao_button = QtWidgets.QPushButton("Projeção", self.centralwidget)
        self.selecao_button = QtWidgets.QPushButton("Seleção", self.centralwidget)
        self.uniao_button = QtWidgets.QPushButton("União", self.centralwidget)
        self.diferenca_button = QtWidgets.QPushButton("Diferença", self.centralwidget)
        self.produto_button = QtWidgets.QPushButton("Produto Cartesiano", self.centralwidget)

        self.gridLayout.addWidget(self.projecao_button, 1, 0)
        self.gridLayout.addWidget(self.selecao_button, 1, 1)
        self.gridLayout.addWidget(self.uniao_button, 2, 0)
        self.gridLayout.addWidget(self.diferenca_button, 2, 1)
        self.gridLayout.addWidget(self.produto_button, 3, 0, 1, 2)

        # Campo de Exibição
        self.resultado_text = QtWidgets.QTextEdit(self.centralwidget)
        self.resultado_text.setReadOnly(True)
        self.gridLayout.addWidget(self.resultado_text, 4, 0, 1, 2)

        # Conectar botões com funções
        self.projecao_button.clicked.connect(self.executarProjecao)
        self.selecao_button.clicked.connect(self.executarSelecao)
        self.uniao_button.clicked.connect(self.executarUniao)
        self.diferenca_button.clicked.connect(self.executarDiferenca)
        self.produto_button.clicked.connect(self.executarProdutoCartesiano)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def exibir_resultado(self, resultado):
        """Função para exibir o resultado no QTextEdit."""
        self.resultado_text.clear()
        if resultado:
            for item in resultado:
                self.resultado_text.append(str(item))
        else:
            self.resultado_text.append("Nenhum resultado encontrado.")

    def executarProjecao(self):
        """Executa a operação de Projeção."""
        # Exemplo de projeção de apenas os nomes dos clientes
        clientes = session.query(Cliente.nome).all()
        self.exibir_resultado(clientes)

    def executarSelecao(self):
        """Executa a operação de Seleção (filtrando por condição)."""
        nome_cliente = "João"  # Defina o nome para a condição de seleção
        clientes = session.query(Cliente).filter(Cliente.nome == nome_cliente).all()
        self.exibir_resultado(clientes)

    def executarUniao(self):
        """Executa a operação de União (união de duas consultas)."""
        # Exemplo de união entre os clientes que têm um nome específico
        clientes1 = session.query(Cliente.nome).filter(Cliente.nome == "João").all()
        clientes2 = session.query(Cliente.nome).filter(Cliente.nome == "Maria").all()
        # Como SQLite não tem suporte direto a UNION, vamos simular combinando os resultados manualmente
        uniao = list(set(clientes1 + clientes2))
        self.exibir_resultado(uniao)

    def executarDiferenca(self):
        """Executa a operação de Diferença (subtração de um conjunto de outro)."""
        # Exemplo: clientes que têm o nome João, mas não têm Maria
        clientes_joao = session.query(Cliente.nome).filter(Cliente.nome == "João").all()
        clientes_maria = session.query(Cliente.nome).filter(Cliente.nome == "Maria").all()
        diferenca = list(set(clientes_joao) - set(clientes_maria))
        self.exibir_resultado(diferenca)

    def executarProdutoCartesiano(self):
        """Executa a operação de Produto Cartesiano entre Cliente e Animal."""
        # Exemplo de produto cartesiano: combina todos os clientes com todos os animais
        clientes = session.query(Cliente).all()
        animais = session.query(Animal).all()
        produto = [(cliente.nome, animal.nome) for cliente in clientes for animal in animais]
        self.exibir_resultado(produto)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Criar a janela principal
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
