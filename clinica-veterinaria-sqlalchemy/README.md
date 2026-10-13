# Clínica Veterinária com SQLAlchemy (ORM)

Mapeamento objeto-relacional em Python com SQLAlchemy para uma clínica veterinária. Os dados ficam em um banco SQLite local, e trocar para MySQL exige só mudar a `DATABASE_URL` em `config.py`.

## Entidades
`Cliente` 1—N `Animal`; `Animal` 1—N `Consulta` N—1 `Veterinario`.

## Arquivos
- `models.py`: classes mapeadas (tabelas `clientes`, `animais`, `veterinarios`, `consultas`).
- `config.py`: engine e sessão.
- `app.py`: cria as tabelas, insere dados de exemplo e lista as consultas via ORM.

## Como rodar
```bash
pip install sqlalchemy
python app.py
```
Saída esperada: `Animal: Cody, Veterinário: Dra. Sabrina, Data: ...`

## Tecnologias
Python 3, SQLAlchemy, SQLite.
