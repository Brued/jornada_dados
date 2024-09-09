# Calcular Desvio Padrão de uma Lista

def calcular_desvio_padrao(lista: list[float]) -> float:
    media = sum(lista) / len(lista)
    variancia = sum((x - media) ** 2 for x in lista) / len(lista)
    return variancia ** 0.5