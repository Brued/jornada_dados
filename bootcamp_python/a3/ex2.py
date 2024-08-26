# Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. 
# Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

#receber temp
    #analisar
temp = float(input("Digite o valor da temperatura(ºC): "))
if temp < 18:
    print(f"A temperatura {temp} é baixa.")
elif 18 >= temp <= 26:
    print(f"A temperatura {temp} é normal.")
else:
    print(f"A temperatura {temp} é alta.")