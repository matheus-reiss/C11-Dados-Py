import numpy as np

# Matriz de exemplo
matriz = np.arange(12).reshape(3, 4) 

print("Matriz:\n", matriz)

# Pegando Linhas e colunas
linhas, colunas = matriz.shape
print(f"Linhas: {linhas}, Colunas: {colunas}")

# Calculando total de elementos
total = linhas * colunas
print("Total de elementos:", total)

# Verificando se é par ou impar
if total % 2 == 0:
    print("O vetor resultante unidimensional teria um número PAR de elementos.")
else:
    print("O vetor resultante unidimensional teria um número ÍMPAR de elementos.")
