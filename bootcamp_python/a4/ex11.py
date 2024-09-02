# Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

def somar_numeros(lista):
    s = 0
    for n in lista:
        s += n
    return s


numeros=[1, 100, 10]
soma = somar_numeros(numeros)
print(soma)