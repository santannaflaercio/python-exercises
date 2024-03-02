def compare_values():
    """
    Compares two values entered by the user and returns a string indicating the relationship between them.

    Returns:
        str: A string indicating the relationship between the two values.
    Raises:
        ValueError: If the user enters invalid values.
    """
    try:
        primeiro_valor = input("Digite o primeiro valor: ")
        segundo_valor = input("Digite o segundo valor: ")

        if primeiro_valor == segundo_valor:
            return f"{primeiro_valor} e {segundo_valor} são iguais"

        if primeiro_valor > segundo_valor:
            return f"{primeiro_valor} é maior que {segundo_valor}"

        return f"{segundo_valor} é maior que {primeiro_valor}"

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos.")


print(compare_values())
