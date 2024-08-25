# Exercício 1: Verificação de Qualidade de Dados Você está analisando um conjunto de dados de vendas
# e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. Escreva 
# um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

# quantidade = int(input("Insira a quantidade: "))
# preco = int(input(" Insiea o preço. "))

# if quantidade > 0 and preco > 0:
#     print("Valores válidos!")
# else:
#     print ("Valor inválido!")   

# Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. 
# Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'


# temp = float(input ("Valor da temperatura º C: "))

# if temp < 18 :
#     print (f"A temperatura {temp} é baixa.")
# elif  18 <= temp <= 26 :
#     print(f"A temperatura {temp} é normal.")
# else:
#     print (f"A temperatura {temp} é alta.")

# Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. 
# Dado um registro de log em formato de dicionário como 
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if log['level'] =='ERROR':
#     print(log['message'])

# Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação,
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. 
# Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# import re

# regra = r"^[A-Z0-9\._+ '\"-]+\@[A-Z0-9]+\.[A-Z0-9]+"
# idade = float(input("Digite sua idade: "))
# email= input("Digite seu email: ").upper()

# if not 18 <= idade <= 65:
#     print("Idade fora do intervalo.")
# elif not re.search (regra, email):
#     print ("Email inválido.")
# else:
#     print("Dados de usuário válidos.")


# MANEIRA LUCIANO

# idade = 25  # Exemplo de valor, substitua com input do usuário se necessário
# email = "usuario@exemplo.com"  # Exemplo de valor, substitua com input do usuário se necessário

# if not 18 <= idade <= 65:
#     print("Idade fora do intervalo permitido")
# elif "@" not in email or "." not in email:
#     print("Email inválido")
# else:
#     print("Dados de usuário válidos")

#  Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. 
# Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário 
# comercial (antes das 9h ou depois das 18h). Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, 
# verifique se ela é suspeita.

#transacao = {'valor': 12000, 'hora': 20}

# valor for superior a R$ 10.000
# if transacao['valor'] > 10000:
#     print(" Limite de transação.")
# elif 9 <= transacao['hora'] <= 18:
#     print("Horario não permitido")


# fora do horário  comercial (antes das 9h ou depois das 18h)

transacao = {'valor': 12000, 'hora': 20}

if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
    print("Transação suspeita")
else:
    print("Transação normal")