# Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.


def inverter_str(txt):
    if len(txt) ==0 :
        print('Digite algo!')
    else:
        texto_invertido =  txt[::-1]
        return texto_invertido
    
texto = 'bruno'
print(inverter_str(texto))