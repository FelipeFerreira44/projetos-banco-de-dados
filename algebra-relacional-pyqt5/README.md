# Operadores de Álgebra Relacional com SQLAlchemy e PyQt5

Interface gráfica que executa, sobre o banco da clínica veterinária, os operadores: projeção, seleção, união, diferença e produto cartesiano.

## Arquivos
- `models.py`: modelos SQLAlchemy (Cliente, Animal, Veterinario, Consulta).
- `tde3comandos.py`: janela PyQt5 com um botão por operador e área de resultado.

## Como rodar
```bash
pip install sqlalchemy pyqt5
python tde3comandos.py
```
O banco `clinica_veterinaria.db` (SQLite) é criado na primeira execução. Cadastre alguns clientes (por exemplo "João" e "Maria") para ver os resultados, porque os filtros de exemplo usam esses nomes.

## Tecnologias
Python 3, SQLAlchemy, PyQt5, SQLite.
