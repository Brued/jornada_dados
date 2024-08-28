### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

dic1 = {'nome': 'Bruno', 'sexo': 'M'}
dic2 = {'nome': 'João', 'idade': 19, 'sexo': 'M'}
dic3 = {'nome': 'Pedro', 'idade': 19, 'sexo': 'M'}

lista = [dic1, dic2, dic3]
print('---=== ANÁLISE DE DADOS FALTANTES ===---')
for valor in lista:
    print('='*40)
    if 'nome' in valor and valor['nome']:
        print(f"{valor['nome']} preencheu seu nome corretamente.")
    else:
        print("Faltou alguém preencher o nome!")

    if 'idade' in valor and valor['idade'] is not None:
        print(f"{valor['nome']} preencheu sua idade {valor['idade']} corretamente. ")
    else:
         print(f"{valor['nome']} faltou preencher sua idade.")

    if 'sexo' in valor and valor['sexo'] is not None:
        print(f"{valor['nome']} preencheu seu sexo {valor['sexo']} corretamente. ")
    else:
         print(f"{valor['nome']} faltou preencher seu sexo.")
    print('='*40)
