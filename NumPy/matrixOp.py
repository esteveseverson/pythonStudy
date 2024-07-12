import numpy as np

def gerar_matriz_aleatoria():
    # Dimensões da matriz
    linhas = 3
    colunas = 3
    # Escopo de valores
    minimo = 0
    maximo = 10
    return np.random.randint(minimo, maximo + 1, (linhas, colunas))

def soma_matrizes(matriz1, matriz2):
    return np.add(matriz1, matriz2)

def sub_matrizes(matriz1, matriz2):
    return np.subtract(matriz1, matriz2)

def produto_matrizes(matriz1, matriz2):
    return np.dot(matriz1, matriz2)

def matriz_inversa(matriz1, matriz2):
    try:
        inv1 = np.linalg.inv(matriz1)
        print(f"A matriz inversa da matriz 1 é:\n{inv1}\n")
    except np.linalg.LinAlgError:
        print("A matriz 1 não é invertível.\n")
    
    try:
        inv2 = np.linalg.inv(matriz2)
        print(f"A matriz inversa da matriz 2 é:\n{inv2}\n")
    except np.linalg.LinAlgError:
        print("A matriz 2 não é invertível.\n")

def matriz_determinante(matriz1, matriz2):
    det1 = np.linalg.det(matriz1)
    det2 = np.linalg.det(matriz2)
    print(f"O determinante da matriz 1 é: {det1}\n")
    print(f"O determinante da matriz 2 é: {det2}\n")
    
# Exemplo de uso
matriz1 = gerar_matriz_aleatoria()
matriz2 = gerar_matriz_aleatoria()

print("Matriz 1:\n", matriz1, "\n")
print("Matriz 2:\n", matriz2, "\n")

print("A soma das matrizes é:\n", soma_matrizes(matriz1, matriz2), "\n")
print("A subtração das matrizes é:\n", sub_matrizes(matriz1, matriz2), "\n")
print("A multiplicação das matrizes é:\n", produto_matrizes(matriz1, matriz2), "\n")
matriz_inversa(matriz1, matriz2)
matriz_determinante(matriz1, matriz2)
