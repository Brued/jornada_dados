### Exercício 12. Validação de Entrada # Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

num = int(input('Digite um número entre 0 a 10: '))
while num > 0:
    if num < 1 or num > 10:
        print('Por favor, digite novamente um número de 0 a 10: ')
        num = int(input('Digite um número: '))
    else:
        print('Entrada válida.')
        break
        

