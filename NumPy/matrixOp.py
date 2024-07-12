import numpy as np

def gerar_matriz_aleatoria():
    #dimenções da matriz
    linhas = 3
    colunas = 3
    #escopo de valores
    minimo = 0
    maximo = 10
    return np.random.randint(minimo, maximo + 1, (linhas, colunas))

def soma_matrizes(matriz_aleatoria1, matriz_aleatoria2):
    return np.add(matriz_aleatoria1, matriz_aleatoria2)

def sub_matrizes(matriz_aleatoria1, matriz_aleatoria2):
    return np.subtract(matriz_aleatoria1, matriz_aleatoria2)

def produto_matrizes(matriz_aleatoria1, matriz_aleatoria2):
    return matriz_aleatoria1 @ matriz_aleatoria2
    #return np.dot(matriz_aleatoria1, matriz_aleatoria2)

def matriz_inversa(matriz_aleatoria1, matriz_aleatoria2):
    print(f" A matriz inversa da matriz 1 é:\n{np.linalg.inv(matriz_aleatoria1)}\n")
    print(f" A matriz inversa da matriz 2 é:\n{np.linalg.inv(matriz_aleatoria2)}\n")

def matriz_determinante(matriz_aleatoria1, matriz_aleatoria2):
    print(f"O determinante da matriz 1 é: {np.linalg.det(matriz_aleatoria1)}")
    print(f"O determinante da matriz 2 é: {np.linalg.det(matriz_aleatoria2)}")
    
# Exemplo de uso
matriz_aleatoria1 = gerar_matriz_aleatoria()
matriz_aleatoria2 = gerar_matriz_aleatoria()
print(matriz_aleatoria1, "\n")
print(matriz_aleatoria2, "\n")

print(f"A o valor da soma das matrizes é:\n{soma_matrizes(matriz_aleatoria1,matriz_aleatoria2)}\n")
print(f"A o valor da subtração das matrizes é:\n{sub_matrizes(matriz_aleatoria1,matriz_aleatoria2)}\n")
print(f"A o valor da multiplicação das matrizes é:\n{produto_matrizes(matriz_aleatoria1,matriz_aleatoria2)}\n")
matriz_inversa(matriz_aleatoria1, matriz_aleatoria2)
matriz_determinante(matriz_aleatoria1, matriz_aleatoria2)

