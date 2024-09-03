"""
Crie uma lista de strings que representam nomes de diferentes frutas. Use uma função
lambda em conjunto com sorted() para ordenar essa lista em ordem alfabética
inversa (do Z ao A).

Instruções:

    Crie uma lista de strings com nomes de frutas.
    Use a função sorted() para ordenar a lista. Para fazer isso em ordem alfabética
    inversa, use uma função lambda como chave de ordenação.
    Imprima a lista ordenada.

frutas = ["banana", "maçã", "laranja", "uva", "abacaxi"]

"""

frutas = ["banana", "maçã", "laranja", "uva", "abacaxi"]

# Ordena a lista de frutas em ordem alfabética inversa (do Z ao A)
ordem_inversa = sorted(frutas, reverse=True)


# Exibe a lista ordenada em ordem alfabética inversa
print(ordem_inversa)