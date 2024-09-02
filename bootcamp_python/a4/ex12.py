
# Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.

def is_prime (numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero %2 == 0:
        return False
    if numero %3 !=0:
        return True

num = 5
print(is_prime(num))