# contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

string = " amo física"
dic = {}

for caractere in string:
    if caractere in dic:
        dic[caractere] += 1
    else:
        dic[caractere] = 1
print(dic)