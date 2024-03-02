def calcular_imc(altura, peso):
    """
    Calculates the Body Mass Index (BMI) based on the given height and weight.

    Args:
        altura (float): The height of the person in meters.
        peso (float): The weight of the person in kilograms.

    Returns:
        float: The calculated BMI value.

    """
    imc = peso / (altura**2)
    return imc


nome = "Laércio Filho"
altura = 1.65
peso = 70

imc = calcular_imc(nome, altura, peso)

print(nome, "tem", altura, "de altura")
print("Ele pesa", peso, "kg")
print("E seu IMC é:", round(imc, 2))
