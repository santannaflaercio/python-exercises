nome_usuario = input("Digite seu nome: ")
idade_usuario = input("Digite sua idade: ")

if (
    nome_usuario is not None
    and nome_usuario != ""
    and idade_usuario is not None
    and idade_usuario.isdigit()
    and int(idade_usuario) > 0
):

    # Imprime o nome do usuário
    print(f"Seu nome é {nome_usuario}")

    # Inverte o nome do usuário
    print(f"Seu nome invertido é {nome_usuario[::-1]}")

    # Verifica se o nome do usuário tem ou não espaços
    if " " in nome_usuario:
        print("Seu nome tem espaços")
    else:
        print("Seu nome não tem espaços")

    # Imprime a quantidade de letras do nome do usuário
    print(f"Seu nome tem {len(nome_usuario)} letras")

else:
    print("Desculpe, você deixou campos vazios.")
