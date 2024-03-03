def encontrar_letras_mais_frequentes(string):
    """
    Retorna uma lista das letras mais frequentes em uma string.

    Args:
        string (str): A string de entrada.

    Returns:
        list: Uma lista contendo as letras mais frequentes na string.
    """
    contador = {}
    max_frequencia = 0

    for letra in string:
        if letra.isalpha():
            contador[letra] = contador.get(letra, 0) + 1
            max_frequencia = max(max_frequencia, contador[letra])

    letras_mais_frequentes = [
        letra for letra, frequencia in contador.items() if frequencia == max_frequencia
    ]
    return letras_mais_frequentes


# Exemplo de uso
string = "abracadabra"
letras_mais_frequentes = encontrar_letras_mais_frequentes(string)

if len(letras_mais_frequentes) == 1:
    print(f"A letra mais frequente na string '{string}' é: {letras_mais_frequentes[0]}")
else:
    print(
        f"As letras mais frequentes na string '{string}' são: {', '.join(letras_mais_frequentes)}"
    )
