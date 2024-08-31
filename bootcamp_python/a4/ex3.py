# Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]

pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa['nome'])
print(pessoas_ordenadas)