import sqlite3
from pathlib import Path

CAMINHO_DB = Path(__file__).resolve().parent.parent / 'data' / 'funcionarios.db'


def conectar():
    return sqlite3.connect(CAMINHO_DB)