# Objetivo: Processar list de uma lista até encontrar um valor específico que indica a parada.

list = [ 'a', 'b', 'parar', 'c', 9, 7]
valor_parada = 'parar'


i = 0
while i < len(list):
    item = list[i]
    if item == valor_parada:
        print(f"Valor de parada encontrado: {item}. Encerrando o processamento.")
        break
    else:
        print(f"Processando item: {item}")
    i += 1
else:
    print("Valor de parada não encontrado na lista.")
