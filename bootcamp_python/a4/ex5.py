# Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

valores = list( 1, 4, 6, 3, 5, 7, 10, 20)
pares = list(valor for valor in valores if valor %2 ==0)
impares = list(valor for valor in valores if valor %2 !=0)