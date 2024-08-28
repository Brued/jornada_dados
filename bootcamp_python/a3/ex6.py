#  Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

txt = str(input('Digite um texto: ')).strip()
palavras = txt.split()
contagem = {}
for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1 
    else:
        contagem[palavra] = 1
print('Contagem de palavras: ')
for palavra, c in contagem.items():
    print(f" → '{palavra}': {c}")