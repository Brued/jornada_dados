### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

lista = list()
list_par = list()
n = int(input('Digite um número: '))
while True:
    lista.append(n)
    op = str(input('Deseja continuar?[S/N]')).upper()
    if op == 'S':
        n = int(input('Digite um número: '))
    elif op == 'N':
        break
print(f" Minha lista é {lista}")

for num in lista:
    if num % 2 == 0:
        list_par.append(num)
print(f"Os números pares na lista são: {list_par}")