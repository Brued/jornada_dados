# Converter Celsius para Fahrenheit em uma Lista

def converter_celsius_fahrenheit(lista_celsius: list[float]) -> list[float]:
    return [(9/5) * temp + 32 for temp in lista_celsius]
