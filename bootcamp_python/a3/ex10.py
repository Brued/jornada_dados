### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# Lista de registros de vendas
registro_ele = list()
registro_per = list()
registros_vendas = [
    {
        'Data': '2024-08-01',
        'Produto': 'Laptop',
        'Categoria': 'Eletrônicos',
        'Quantidade': 2,
        'Preço': 2500.00
    },
    {
        'Data': '2024-08-02',
        'Produto': 'Mouse',
        'Categoria': 'Periféricos',
        'Quantidade': 5,
        'Preço': 50.00
    },
    {
        'Data': '2024-08-03',
        'Produto': 'Teclado',
        'Categoria': 'Periféricos',
        'Quantidade': 3,
        'Preço': 100.00
    },
    {
        'Data': '2024-08-04',
        'Produto': 'Monitor',
        'Categoria': 'Eletrônicos',
        'Quantidade': 1,
        'Preço': 800.00
    }
]

s_ele = s_per = 0
# Definir novos dic por categoria:
for registro in registros_vendas:
    if registro['Categoria'] == 'Eletrônicos':
        registro_ele.append(registro)
    elif registro['Categoria'] == 'Periféricos':
        registro_per.append(registro)

print('-'*40)
print("Registros da Categoria 'Eletrônicos':")
print('-'*40)
for registro in registro_ele:
    s_ele += registro['Quantidade']
    print(f"Produto: {registro['Produto']}, Quantidade: {registro['Quantidade']}")
print(f"\n→ Total de Quantidade de Produtos 'Eletrônicos': {s_ele}")

print('-'*40)
print("Registros da Categoria 'Periféricos':")
print('-'*40)
for registro in registro_per:
    s_per += registro['Quantidade']
    print(f"Produto: {registro['Produto']}, Quantidade: {registro['Quantidade']}")
print(f"\n→ Total de Quantidade de Produtos 'Periféricos': {s_per}")




