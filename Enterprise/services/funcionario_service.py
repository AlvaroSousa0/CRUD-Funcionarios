from repositories.funcionario_repository import (adicionar, listar, buscar_id, buscar_nome, remover)
from models.funcionario import Funcionario
from utils.validators import validar_email

def cadastrar_funcionario(
        nome,
        idade,
        email,
        contato,
        endereco,
        cargo
):

    if not nome.strip():
        print('O nome não pode estar vazio.')
        return
    
    if idade <= 0:
        print('Idade inválida.')
        return
    
    if not validar_email(email):
        print('Email inválido.')
        return
    
    if not contato.strip():
        print('Contato inválido.')
        return
    
    if not endereco.strip():
        print('Endereço inválido')
        return
    
    if not cargo.strip():
        print('cargo inválido')
        return
    
    funcionario = Funcionario(
        nome=nome,
        idade=idade,
        email=email,
        contato=contato,
        endereco=endereco,
        cargo=cargo
    )

    adicionar(funcionario)


    print('Funcionario cadastrado com sucesso.')

def listar_funcionarios():
    funcionarios = listar()

    if not funcionarios:
        print('Nenhum funcionário encontrado.')
        return

    for funcionario in funcionarios:

        print(f"""
        ID: {funcionario.id}
        Nome: {funcionario.nome}
        Cargo: {funcionario.cargo}
    """)

def buscar_por_id(id_funcionario):
    funcionario = buscar_id(id_funcionario)

    if funcionario is None:
        print('Funcionário não encontrado')
        return
    
    print(f"""
        ID: {funcionario.id}
        Nome: {funcionario.nome}
        Idade: {funcionario.idade}
        Cargo: {funcionario.cargo}
        Telefone: {funcionario.telefone}
        Email: {funcionario.email}
        Endereço: {funcionario.enedereco}
    """)

def buscar_por_nome(nome_funcionario):
    funcionario = buscar_nome(nome_funcionario)

    if funcionario is None:
        print('Funcionário não encontrado')
        return
    
    print(f"""
        ID: {funcionario.id}
        Nome: {funcionario.nome}
        Idade: {funcionario.idade}
        Cargo: {funcionario.cargo}
        Telefone: {funcionario.telefone}
        Email: {funcionario.email}
        Endereço: {funcionario.enedereco}
    """)

def atualizar_funcionario():
    pass

def remover_funcionario(id_funcionario):

    buscar_por_id(id_funcionario)
    while True:

        confirma = input(
            'Confirma remoção? (S/N): '
        ).strip().upper()

        if confirma == 'S':

            remover(id_funcionario)

            print('Funcionário removido.')

            break

        elif confirma == 'N':

            print('Funcionário não removido.')

            break

        else:

            print('Digite apenas S ou N.')
        
