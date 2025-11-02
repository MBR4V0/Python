# Sistema de Reserva de Equipamentos Audiovisuais

# Lista para armazenar os equipamentos
equipamentos = []

# Função para cadastrar um novo equipamento
def cadastrar_equipamento():
    nome = input("Digite o nome do equipamento: ")
    equipamento = {
        "id": len(equipamentos) + 1,
        "nome": nome,
        "disponivel": True,
        "reservado_por": "",
        "data_reserva": ""
    }
    equipamentos.append(equipamento)
    print("Equipamento cadastrado com sucesso!")

# Função para listar todos os equipamentos
def listar_equipamentos():
    if not equipamentos:
        print("Nenhum equipamento cadastrado.")
        return

    print("\nLista de Equipamentos:")
    for equip in equipamentos:
        status = "Disponível" if equip["disponivel"] else "Reservado"
        print(f"ID: {equip['id']} | Nome: {equip['nome']} | Status: {status}")
        if not equip["disponivel"]:
            print(f"Reservado por: {equip['reservado_por']} | Data: {equip['data_reserva']}")

# Função para reservar um equipamento
def reservar_equipamento():
    listar_equipamentos()
    if not equipamentos:
        return

    try:
        id = int(input("\nDigite o ID do equipamento que deseja reservar: "))
        equipamento = next((equip for equip in equipamentos if equip["id"] == id), None)

        if equipamento is None:
            print("ID inválido!")
            return

        if not equipamento["disponivel"]:
            print("Equipamento já está reservado!")
            return

        nome_prof = input("Digite seu nome: ")
        data = input("Digite a data da reserva (DD/MM/AAAA): ")

        equipamento["disponivel"] = False
        equipamento["reservado_por"] = nome_prof
        equipamento["data_reserva"] = data
        print("Reserva realizada com sucesso!")

    except ValueError:
        print("Por favor, digite um ID válido (número inteiro).")

# Função para liberar um equipamento
def liberar_equipamento():
    listar_equipamentos()
    if not equipamentos:
        return

    try:
        id = int(input("\nDigite o ID do equipamento a ser liberado: "))
        equipamento = next((equip for equip in equipamentos if equip["id"] == id), None)

        if equipamento is None:
            print("ID inválido!")
            return

        if equipamento["disponivel"]:
            print("Equipamento já está disponível!")
            return

        equipamento["disponivel"] = True
        equipamento["reservado_por"] = ""
        equipamento["data_reserva"] = ""
        print("Equipamento liberado com sucesso!")

    except ValueError:
        print("Por favor, digite um ID válido (número inteiro).")

# Menu principal
def menu():
    while True:
        print("\n=== Sistema de Reserva de Equipamentos ===")
        print("1. Cadastrar Equipamento")
        print("2. Listar Equipamentos")
        print("3. Reservar Equipamento")
        print("4. Liberar Equipamento")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_equipamento()
        elif opcao == "2":
            listar_equipamentos()
        elif opcao == "3":
            reservar_equipamento()
        elif opcao == "4":
            liberar_equipamento()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    menu()
