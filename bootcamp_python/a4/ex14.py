# Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.

# def combinacao_pares(list, num):
def encontrar_pares(lista, alvo):
    """Encontra todos os pares na lista que somam ao número alvo."""
    vistos = set()   # Conjunto para armazenar números vistos
    pares = []       # Lista para armazenar os pares encontrados

    for numero in lista:
        complemento = alvo - numero
        if complemento in vistos:
            pares.append((complemento, numero))
        vistos.add(numero)
    
    return pares

print(encontrar_pares([1,2,4, 5, 2, 3], 4))