import numpy as np
import matplotlib.pyplot as plt

# Gerar um conjunto de dados original
x = np.linspace(0, 20, num=21)
y = np.sin(x)

# Introduzir valores faltantes
y[3] = np.nan
y[6] = np.nan
y[8] = np.nan

print("Dados originais com valores faltantes:")
print(y)

# Interpolação Linear
indices_validos = ~np.isnan(y)
indices_faltantes = np.isnan(y)
y_interp_linear = np.copy(y)
y_interp_linear[indices_faltantes] = np.interp(x[indices_faltantes], x[indices_validos], y[indices_validos])

print("Dados após interpolação linear:")
print(y_interp_linear)

# Interpolação Polinomial
coeficientes_polinomio = np.polyfit(x[indices_validos], y[indices_validos], 3)
polinomio = np.poly1d(coeficientes_polinomio)
y_interp_polinomial = np.copy(y)
y_interp_polinomial[indices_faltantes] = polinomio(x[indices_faltantes])

print("Dados após interpolação polinomial:")
print(y_interp_polinomial)

# Plotar os resultados
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Dados Originais com Faltantes')
plt.plot(x, y_interp_linear, '-', label='Interpolação Linear')
plt.plot(x, y_interp_polinomial, '--', label='Interpolação Polinomial')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolação de Dados Faltantes')
plt.show()
