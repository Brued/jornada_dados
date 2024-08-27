# Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação,
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. 
# Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# entrada idade e email:
idade = int(input("Digite sua idade: "))
email = str(input("Digite seu email: ")).strip()


#validar
if 18 >= idade <= 65 :
    print("Erro: Idade de usuário inválido")
else:
    if '@' not in email or '.' not in email:
        print("Erro: O email fornecido não é válido.")
    else:
        antes, depois = email.split("@", 1)
        if '.' not in depois:
            print("Erro: O email não é válido.")
        else:
            print("Dados de usuário válidos.")

