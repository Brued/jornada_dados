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

raio = float(input("Qual o valor do raio do circulo?"))
area = math.pi * raio ** 2
print(f"A area desse circulo é dada por:{area:.2f} ")


