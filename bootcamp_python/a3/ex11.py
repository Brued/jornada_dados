### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.



nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
sexo = str(input('Digite seu sexo: '))

op = str(input("Digite algo ou para sair digite 'sair': ")).lower()
while op != 'sair':
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: '))

    op = str(input("Digite algo ou para sair digite 'sair': ")).lower()
    if op == 'sair':
        break