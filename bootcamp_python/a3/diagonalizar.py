
import numpy as np

import sympy as sp

# Defina as variáveis simbólicas
del_t, m, nabla = sp.symbols('del_t m nabla', real=True)

# Defina a expressão para a11
a11 = del_t**2 + (m**4) / (16 * (-nabla**2 + m**2 / 4))

# Defina a expressão para a12
a12 = (nabla**2 - (m**2 * nabla**2) / (-nabla**2 + m**2 / 4)) * del_t

# a21 é igual a -a12
a21 = -a12

# Defina a expressão para a22
a22 = (-nabla**2 * del_t**2) / (-nabla**2 + m**2 / 4) + (m**2 - nabla**2) * nabla**2

# Imprimir os resultados
print("a11 =", a11)
print("a12 =", a12)
print("a21 =", a21)
print("a22 =", a22)


# Defina a matriz
A = np.array([[a11, a12],
              [a21, a22]])

# Calcule os autovalores e autovetores
eigenvalues, eigenvectors = np.linalg.eig(A)

# Crie a matriz diagonal dos autovalores
D = np.diag(eigenvalues)

# A matriz de autovetores
P = eigenvectors

# A matriz inversa de P
P_inv = np.linalg.inv(P)

# Reconstrua a matriz original
A_reconstructed = P @ D @ P_inv

print("Matriz original:")
print(A)

print("\nAutovalores:")
print(eigenvalues)

print("\nMatriz de autovetores (P):")
print(P)

print("\nMatriz diagonal dos autovalores (D):")
print(D)

print("\nMatriz reconstruída:")
print(A_reconstructed)

# a11 = del_t ^2 + (m^4)/(16(-nabla^2 + m^2/4))

# a12 = (nabla^2 - (m^2 *nabla^2)/(-nabla^2 + m^2/4))del_t
# a21 = - a12

# a22 = (-nabla^2 del_t^2)/ -nabla^2 + m^2/4 + (m^2 - nabla^2) nabla^2
