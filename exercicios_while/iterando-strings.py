"""
Iterando strings com while
"""

nome = "Jean Carlos"
# Cria uma lista com cada letra do nome
array_nome = list(nome)


# Concatenando string para formatar o texto com o seguinte padrão: *L*a*é*r*c*i*o*
nome_formatado = "*".join(array_nome)
nome_formatado = "*" + nome_formatado + "*"
print(nome_formatado)
