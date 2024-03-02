"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro. Caso o usuário não digite um número inteiro, informe que o número informado não é um inteiro.
"""

numero = input("Digite um número inteiro: ")

if not numero.isdigit():
    print("O número informado não é um inteiro")
else:
    numero = int(numero)
    if numero % 2 == 0:
        resultado = "par"
    else:
        resultado = "ímpar"

    print(f"O número é {resultado}")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input("Digite a hora atual: ")

if not hora.isdigit() or int(hora) < 0 or int(hora) > 23:
    print("O valor informado não corresponde ao formato de hora")
else:
    hora = int(hora)
    if hora < 12:
        print("Bom dia")
    elif hora < 18:
        print("Boa tarde")
    else:
        print("Boa noite")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input("Digite o seu primeiro nome: ")

tamanho = len(nome)
if tamanho <= 4:
    mensagem = "curto"
elif tamanho <= 6:
    mensagem = "normal"
else:
    mensagem = "muito grande"

print(f"Seu nome é {mensagem}")
