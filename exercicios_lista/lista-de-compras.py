lista_de_compras = []


def adicionar_item(item):
    lista_de_compras.append(item)
    print(f"{item} foi adicionado à lista de compras.")


def remover_item(item):
    if item in lista_de_compras:
        lista_de_compras.remove(item)
        print(f"{item} foi removido da lista de compras.")
    else:
        print(f"{item} não está na lista de compras.")


def listar_itens():
    if lista_de_compras:
        print("Itens na lista de compras:")
        for item in lista_de_compras:
            print(item)
    else:
        print("A lista de compras está vazia.")


while True:
    print("\nO que você deseja fazer?")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Listar itens")
    print("4 - Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        item = input("Digite o item que deseja adicionar: ")
        adicionar_item(item)
    elif opcao == "2":
        item = input("Digite o item que deseja remover: ")
        remover_item(item)
    elif opcao == "3":
        listar_itens()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
