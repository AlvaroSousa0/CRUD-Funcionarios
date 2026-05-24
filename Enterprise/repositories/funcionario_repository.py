from database.connection import conectar
from models.funcionario import Funcionario


def adicionar(funcionario: Funcionario):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO funcionarios
        (nome, idade, telefone, email, endereco, cargo)
        VALUES (?, ?, ?, ?, ?, ?)
    """

    cursor.execute(sql, (
        funcionario.nome,
        funcionario.idade,
        funcionario.telefone,
        funcionario.email,
        funcionario.endereco,
        funcionario.cargo
    ))

    conexao.commit()
    conexao.close()

def listar():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM funcionarios")

    resultados = cursor.fetchall()

    funcionarios = []

    for linha in resultados:
        funcionario = Funcionario(
            linha[0],
            linha[1],
            linha[2],
            linha[3],
            linha[4],
            linha[5],
        )
        funcionarios.append(funcionario)

    conexao.close()

    return funcionarios

def buscar_id(id_funcionario):

    conexao = conectar()

    cursor = conexao.cursor()

    sql = """
    SELECT * FROM funcionarios
    WHERE id = ?
    """
    cursor.execute(sql, (id_funcionario,))

    resultado = cursor.fetchone()

    if resultado is None:
        return None
    
    funcionario = Funcionario(
        resultado[1],
        resultado[2],
        resultado[3],
        resultado[4],
        resultado[5],
        resultado[6]
    )

    funcionario.id = resultado[0]

    conexao.close()

    return funcionario

def buscar_nome(nome_funcionario):
   
    conexao = conectar()

    cursor = conexao.cursor()

    sql = """
    SELECT * FROM funcionarios
    WHERE nome = ?
    """
    cursor.execute(sql, (nome_funcionario,))

    resultado = cursor.fetchone()

    if resultado is None:
        return None
    
    funcionario = Funcionario(
        resultado[1],
        resultado[2],
        resultado[3],
        resultado[4],
        resultado[5],
        resultado[6]
    )

    funcionario.id = resultado[0]
    
    conexao.close()
    
    return funcionario

def remover(id_funcionario):
    conexao = conectar()

    cursor = conexao.cursor()

    sql = """
        DELETE FROM funcionarios
        WHERE id = ?
    """

    cursor.execute(sql, (id_funcionario,))

    conexao.commit()

    conexao.close()