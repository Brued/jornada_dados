# Objetivo: Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

max_tentativas = 10
tentativa = 1
while tentativa <= max_tentativas:
    print(f"Tentativa {tentativa} de {max_tentativas}")
    if True:
        print("Conexão realizada")
        break

    tentativa +=1
else:
    print(f"Falha ao conectar após {max_tentativas}")

