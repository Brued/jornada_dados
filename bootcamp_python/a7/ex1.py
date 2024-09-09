# Calcular Média de Valores em uma Lista

def media_list(list: list) -> int:
    s=0
    for n in list:
        s += n
    media= s / len(list)
    return media


