
# Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# x = int (input("Digite o primeiro numero: "))
# y = int (input("Digite o segundo numero: "))
# div = x // y 
# print("O resultado da divisão inteira é: ", div)


# pensando nas possibilidades de erro 
#EXEMPLO QUE CAUSA TypeError


# nome = "Luciano"
# try: 
#     resultado  =len(nome)
#     print(resultado)
# except TypeError as e:
#     print(e) 

# imprimir ok

# try: 
#     resultado  =len(3)
#     print(resultado)
# except TypeError as e:
#     print(e) # imprime a msg de erro
    

# se caso não for um nome da um erro de tipo >>PIOR ERRO QUE PODEMOS TER

# POSSO PRINTA A MSG DE ERRO PRO USER 


# Dois comando uteis

# else:  Caso de tudo bem faça isso ex print ("tudo ocorreu bem")

# finally:  independende disso

# print(" o importante e participar: ")

# isinstance faz um check... avalie pra mim
numero = int(input ("insira um numero: "))
if isinstance (numero, int):
     print("A variável é um inteiro: ")
else:
     print("A variavel não é um inteiro.")