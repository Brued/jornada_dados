# Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
dic1 = {"Thresh" : "Support", "Lucian": "AD Carry"}
dic2 = {"Soraka": "Support", "Ezreal": "AD Carry"}

dict = { **dic1, **dic2}
print(dict)
