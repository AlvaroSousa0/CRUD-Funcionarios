from services.funcionario_service import (
    cadastrar_funcionario,
    listar_funcionarios,
    buscar_por_id,
    buscar_por_nome,
    atualizar_funcionario,
    remover_funcionario
)
from time import sleep

while True:
    print("""
        Ola, seja bem vindo ao Cadastro de Funcionarios da XX Corp!
        """)
    
    
    print("            1 - Adicionar")
    print("            2 - Listar")
    print("            3 - Busca por id")
    print("            4 - Busca por nome")
    print("            5 - Atualizar")
    print("            6 - Remover")
    print("            7 - Sair")

    opcao = input("""
            Escolha a opcao que deseja:""")

    match opcao:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            print("\n     Finalizando a sessão...")
            sleep(1)
            print("     XX Corp agradece a utilização!")
            sleep(0.5)
            print("     Até a proxima!\n")
            sleep(0.5)
            break