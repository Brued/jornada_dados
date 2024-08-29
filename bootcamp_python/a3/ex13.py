  ### Exercício 13. Consumo de API Simulado 
  # Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

pag = 1
total_pgs = 5

while pag <= total_pgs:
    print(f"Processando página {pag} de {total_pgs}")
    pag +=1
print("todas as páginas foram processadas.")