palavra_secreta = "python"
letras_descobertas = []
tentativas = 0
max_tentativas = 6

while True:
    letra = input("Digite uma letra: ")

    if len(letra) != 1:
        print("Por favor, digite apenas uma letra.")
        continue

    letras_descobertas.append(letra)
    tentativas += 1

    palavra_atual = "".join(
        [
            letra_secreta if letra_secreta in letras_descobertas else "*"
            for letra_secreta in palavra_secreta
        ]
    )
    print(palavra_atual)

    if palavra_atual == palavra_secreta:
        print("Parabéns! Você acertou a palavra!")
        break

    print("Tentativas:", tentativas)

    if tentativas >= max_tentativas:
        print(
            "Você excedeu o número máximo de tentativas. A palavra era:",
            palavra_secreta,
        )
        break
