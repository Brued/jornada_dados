import csv
caminho_arquivo = 'partículas.csv'

dados_particulas = []

with open(caminho_arquivo, mode = 'r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    for linha in leitor_csv:
        dados_particulas.append(linha)
for registro in dados_particulas:
    print(registro)