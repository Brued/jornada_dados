# Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas




def keys_order(dict: dict):
    order = sorted(dict.keys())
    return order



dicionario = {
    'alpha': 1200,
    'delta': 1003,
    'gamma': 222,
    'betha': 104
}
print(keys_order(dicionario))