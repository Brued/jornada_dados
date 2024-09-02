# Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.



# função

def find_par(lista: list, alvo: int):
    """"
    lista: Fornece a lista de números
    alvo: Fornce o número pelo o qual as combinações da lista tem que chegar."""
    pares = []
    for n in range(len(lista)): 
        for m in  range(n + 1, len(lista)):
            if lista[n] + lista[m] == s:
                pares.append((lista[n], lista[m]))
    return pares






# main
s = 5
conjunto = [1, 2, 3, 4]

print(f"Para o conjunto listado  encontramos {find_par(conjunto, s)}")