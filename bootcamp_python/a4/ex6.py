# Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]
print("--->> Produtos com valores antigos << ---")
print()
print(produtos)
print()
for produto in produtos:
    if produto["id"] == 1:
        produto["preço"] = 120

print("--->> Produtos atualizados <<---")
print()
print(produtos)