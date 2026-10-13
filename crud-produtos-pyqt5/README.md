# CRUD de Produtos com SQLAlchemy e PyQt5

Aplicação desktop para cadastro de produtos (nome, descrição, preço), com persistência via SQLAlchemy em SQLite.

## Arquivos
- `banco_dados.py`: modelo `Produto`, engine e sessão.
- `operacoes_crud.py`: funções de criar, listar, atualizar e deletar.
- `interface_grafica.py`: janela PyQt5 (hoje com o formulário de criação).

## Como rodar
```bash
pip install sqlalchemy pyqt5
python interface_grafica.py
```

## Próximos passos
- Ligar à interface a listagem, a edição e a exclusão (as funções já existem em `operacoes_crud.py`).
- Validar a entrada de preço.

## Tecnologias
Python 3, SQLAlchemy, PyQt5, SQLite.
