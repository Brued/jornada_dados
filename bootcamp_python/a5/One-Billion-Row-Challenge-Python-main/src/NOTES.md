## Using python

Inicio com um função para processar meus dados
Marcando o tempo de início com a biblioteca time
-Separando pela biblioteca collections usando a função defaltdict()
Defaulttdict() – tipo de dicionário, subclasse de dicionário interno que fornece um valor padrão para as chaves que ainda não foram definidas no dict
Muito útil quando se está lidando com dicionários e precisa evitar a verificação se uma chave existe antes de  acessar outra ou adicionar valores
Biblioteca path – para buscamos nossos dados
Csv reader – leitor dos meus dados em csv
Parte de Api
Finaliza o tempo

## using Pandas
Essencial na D.A.
-DataFrames e Series
-Leitura e Escrita de Dados
-Manipulação de Dados
-Limpeza e Transformação
-Visualização
-Tempo e Datas

## Using Duckdb
Gerenciamento de database embedded 


## Using Polars

Projetada para ser rápida e eficiente -> grandes volumes de dados. 
Principais recursos e conceitos relacionados ao Polars:
-Performance
-API Expressiva
-DataFrames e Series
-Lazy Evaluation
-Suporte a Vários Formatos de Arquivo
-Paralelismo e Multithreading

## Usind Dask
Facilita o processamento paralelo e distribuído de grandes volumes de dados 
Operacoes de PC que não cabem na memória de um único PC
Projetado para escalar de uma única máquina para clusters distribuiídos
-DataFrames
-Arrays
-Delayed
-Distribuição
-Escalabilidade
-Integração com Pandas e NumPy

## Testes
1M
Python  1.59s
Polars 0.21s
Dask 0.72s
Pandas 2.76s
Duckdb 0.29s

10M
Python 13.75s  
Polars 1.93s
Dask 4.76s
Pandas 9.82s
Duckdb 1.41s

