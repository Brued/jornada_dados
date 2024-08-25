CONSTANTE_BONUS = 1000

nome = input("Digite o seu nome: ")
# 1 - Possivel erro seria inserir numero no lugar do nome:
if nome.isdigit():
    print("Você não digitou um nome correto!")
    exit()
    # 2 - A pessoa nao digitar nada.
elif len(nome) == 0 :
    print("Você não digitou nada.")
    exit()


# 3 - salário pode ser negativo
try:
    salario = float(input("Insira o valor do seu salário: "))
    if salario < 0:
        print("você digitou um salário inexistente!")
        exit()     
except ValueError:
        print("você não digitou um numero no salario.")
        exit()


bonus  = float(input ("Digite o seu bonus: "))
                
try: 
     if bonus < 0 :
          print("Você digitou um bonus inválido.")
          exit()
except ValueError:
     print("Você digitou um valor errado.")

valor_do_bonus = CONSTANTE_BONUS + salario * bonus

print (f"O usuário {nome} possui o bonus de {valor_do_bonus}")