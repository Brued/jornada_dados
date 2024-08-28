### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

list = []
n = int(input('Digite um número: '))
while True:
    list.append(n)
    op = str(input('Deseja continuar?[S/N]')).upper()
    if op == 'S':
        n = int(input('Digite um número: '))
    elif op == 'N':
        break
print(list)

max = max(list)
min = min(list)


lista_normalizada = [( valor - min ) / (max - min) for valor in list]

print('='*8)
print(" ---> lista normalizada <---")
print(lista_normalizada)
print('='*8)
