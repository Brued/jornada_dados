# Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

idades = [22, 14, 12, 25, 40, 60, 95]

idades_maiores = []
for i in idades:
    if i >= 18:
        idades_maiores.append(i)
print(idades_maiores)

### opção ##
# idadesmaiores = [ idade for idade in idades if idade>= 18]