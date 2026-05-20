from database.connection import conectar


def adicionar(funcionario):

    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO funcionarios
        (nome, idade, contato, email, endereco, cargo)
        VALUES (?, ?, ?, ?, ?, ?)
    """

    cursor.execute(sql, (
        funcionario.nome,
        funcionario.idade,
        funcionario.contato,
        funcionario.email,
        funcionario.endereco,
        funcionario.cargo
    ))

    conexao.commit()
    conexao.close()

