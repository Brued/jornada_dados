# Inteiros (int)

# 1 - Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# x = int(input("Digite um numero inteiro: "))
# y = int(input("Digite um segundo numero inteiro: "))
#sum = x + y

#print("A Soma dos dois é: ", sum)

# 2 - Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# x = int(input("Digite um numero inteiro: "))
# y = int(input("Digite um segundo numero inteiro: "))
# x = int (input("Digite um numero: "))
# resul = x % 5
# print ("O resto da divisão por 5 é: ", resul)

# 3 - Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
#x = int(input("Digite um numero: "))
#y = int(input("Digite o segundo numero: "))

#mult = x * y 
#print("A multiplicação deles é: ", mult)

# 4 - Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# x = int (input("Digite o primeiro numero: "))
# y = int (input("Digite o segundo numero: "))
# div = x // y 
# print("O resultado da divisão inteira é: ", div)

# 5 - Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# x = int(input("Digite um numero: "))
# resul = x **2
# print("O quadrado dele é: ", resul)

# Números de Ponto Flutuante (float)

# 6 - Escreva um programa que receba dois números flutuantes e realize sua adição.
#x = float (input("Digite um numero: "))
#y = float (input("Digite um numero: "))
#sum = x + y
#print("A soma deles é: ", sum)


# 7 - Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# x = float (input ("Digite um numero: "))
# y = float (input ("Digite um segundo numero: "))
# media = (x + y)/2
# print ("A média deles é: ", media)

# 8 - Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# x = float (input("Digite um numero base: "))
# y = float (input("Digite o expoente: "))
# pot =  x ** y
# print (f"A potencia de {x} elevado a {y} é igual a:  ", pot)    

# 9 Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# temp_celsius= float (input("Digite o valor da temperatura: "))
# temp_fahrenheit = (temp_celsius * 9/5) + 32
# print(f"{temp_celsius} º celsius em Fahrenheit é: ", temp_fahrenheit)

# 10 - Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math

# raio = float(input("Qual o valor do raio do circulo?"))
#  area = math.pi * raio ** 2
# print(f"A

# String

# 11 . Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
 
# texto = input("Digite um texto: ")
# texto_maiuscula = texto.upper()
# print ("Texto em maiúscula: ", texto_maiuscula)


# 12 - Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# nome = input ("Digite o seu nome completo: ")
# nome_minuscula = nome.lower()
# print("O nome em minusculo é: ", nome_minuscula)


# 13 -Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, 
 #imprima esta frase sem espaços em branco no início e no final.

# frase = input("Digite uma frase: ")
# nova_frase = frase.strip()
# print("A nova frase sem espaço no inicio e no final:", nova_frase)

# 14 - Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, 
# imprima o dia, o mês e o ano separadamente.
# dma= input("Digite a data/ mes / ano: ")
# dia, mes, ano = dma.split("/") 
# print("Dia: ", dia)
# print("Mes: ", mes)
# print("Ano: ", ano)

# 15 - Escreva um programa que concatene duas strings fornecidas pelo usuário.
 # string1 = input("Insira a parte um: ")
# string2 = input(" Insira a parte dois: ")
# resultado = string1 + " " + string2
# print("Concatenando: ", resultado)

# 16 - Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário 
# e retorne o resultado da operação AND entre elas.
# Exemplo de entrada
# valor1= input("Insira a primeira expressão bool:")
# valor2 = input("Insira a segunda expressão bool: ")
# resultado_and = valor1 and valor2
# print("Resultado do AND lógico:", resultado_and)

# 17 - Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# valor1= input("Insira a primeira expressão bool:")
# valor2 = input("Insira a segunda expressão bool: ")
# resultado_or = valor1 or valor2
# print("Resultado do OR lógico:", resultado_or)

# 18 - Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor

# valor = input("Insira um valor bool: ")
# novo_valor = not valor
# print("O valor invertido é: ", novo_valor)

#  19 - Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# valor1 = int(input("Digite um numero: "))
# valor2 = int (input("Digite um segundo numero: "))
# comp = valor1 == valor2
# print("Os numeros são iguais: ", comp)
 

 # 20 - Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# valor1 = int(input("Digite um numero: "))
# valor2 = int(input("Digite um segundo numero: "))
# resul_dif= valor1 != valor2
# print("Os numeros são diferente: ", resul_dif)


# 21 - Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa
#  deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir 
# que a entrada seja numérica, tratando qualquer ValueError. 
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.


# try:
#     temp_celsius = float(input("Insira o valor da temperatura em celsius: "))
#     temp_fahrenheit = (temp_celsius * 9/5) + 32
#     print(f"A temperatura em Fahrenheit é: ", temp_fahrenheit)
# except ValueError:
#     print("Digite uma temperatura valida novamente.")

# 21 - Crie um programa que verifica se uma palavra ou frase é um palíndromo
#  (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações).
#  Utilize try-except para garantir que a entrada seja uma string. 
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.



# condição de inverter if palavra == palavra[::-1]:

# palavra_frase = input("Digite uma palavra: ")

# if isinstance (palavra_frase, str):
#      formatado = palavra_frase.replace("", "").lower()
#      if formatado == formatado [::-1]:
#         print("É um Palíndromo.")
#      else: 
#         print("Não é um Palíndromo." )
# else:
#     print("Digite novamente uma palavra ou frase válida.")


# 23. Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para 
# realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.


# try: 
#     entrada1 = float(input("Digite a primeira entrada: "))
#     entrada2 = float(input("Digite a segunda entrada: "))
#     operacao = input("Insira a operação +, -, *, /: ")

# soma
#     if operacao == '+' :
#         resul= entrada1 + entrada2

#     elif  operacao == '-' : 
#         resul = entrada1 - entrada2

#     elif operacao == '*':
#         resul = entrada1 * entrada2

#     elif operacao == '/':
#         if entrada2 != 0 :
#             resul = entrada1 / entrada2

#         else:
#             print("Divisão por zero.")
#             resul = None
#     else: 
#         print("Operador inválido!")
#         resul = None
#     if resul is not None:
#         print("Resultado: ", resul)
# except ValueError:
#     print("Entrada inválida. Insira numeros!")

# 24 - Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize try-except para assegurar que a entrada seja numérica e utilize 
# if-elif-else para classificar o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".


try:
    num = int(input("Insira um número: "))
    if num < 0:
      print("O valor é negativo!")
    elif num > 0:
      print ("O valor é positivo!")
    else: 
      print("O valor é zero!")
    if num % 2 == 0:
         print("Par")
    else:
         print("Ímpar!") 
except ValueError:
   print("Entrada inválida.")
