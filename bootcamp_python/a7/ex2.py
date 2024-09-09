# Filtrar Dados Acima de um Limite

def filtrar_limite(valores: list[float], limite: float) -> float:
    lista_com_limites = 0
    for n in valores:
        if n > limite:
            lista_com_limites.append(n)
        return lista_com_limites