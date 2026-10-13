from banco_dados import Session, Produto

def criar_produto(nome, descricao, preco):
    session = Session()
    produto = Produto(nome=nome, descricao=descricao, preco=preco)
    session.add(produto)
    session.commit()
    session.close()

def listar_produtos():
    session = Session()
    produtos = session.query(Produto).all()
    session.close()
    return produtos

def atualizar_produto(id, novo_nome, nova_descricao, novo_preco):
    session = Session()
    produto = session.query(Produto).get(id)
    if produto:
        produto.nome = novo_nome
        produto.descricao = nova_descricao
        produto.preco = novo_preco
        session.commit()
    session.close()

def deletar_produto(id):
    session = Session()
    produto = session.query(Produto).get(id)
    if produto:
        session.delete(produto)
        session.commit()
    session.close()
