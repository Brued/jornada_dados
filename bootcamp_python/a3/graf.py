import numpy
print(numpy.__version__)


# import numpy as np
# import matplotlib.pyplot as plt

# # Gerar um intervalo de valores de y
# y = np.linspace(-0.5, 1.5, 400)

# # Calcular x para cada valor de y
# x1 = y**2
# x2 = y**3

# # Criar o gráfico
# plt.figure(figsize=(8, 6))
# plt.plot(x1, y, label='$x = y^2$', color='blue')
# plt.plot(x2, y, label='$x = y^3$', color='red')

# # Preencher a área entre as curvas
# plt.fill_betweenx(y, x2, x1, where=(x1 > x2), color='lightgray', alpha=0.5)

# # Ajustar os limites do gráfico
# plt.xlim(-0.1, 1.1)
# plt.ylim(-0.1, 1.1)

# # Adicionar rótulos e título
# plt.xlabel('$x$')
# plt.ylabel('$y$')
# plt.title('Curvas $x = y^2$ e $x = y^3$')
# plt.legend()

# # Mostrar o gráfico
# plt.grid(True)
# plt.axhline(0, color='black',linewidth=0.5)
# plt.axvline(0, color='black',linewidth=0.5)
# plt.show()
