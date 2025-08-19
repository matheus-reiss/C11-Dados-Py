import numpy as np

# Cria matriz 4x4 com seed 10
np.random.seed(10)
matriz = np.random.randint(1, 51, size=(4, 4))

print("Matriz gerada:\n", matriz)

# Media das linhas e colunas
media_linhas = matriz.mean(axis=1)   
media_colunas = matriz.mean(axis=0)

print("\nMédia das linhas:", media_linhas)
print("Média das colunas:", media_colunas)

# Maior valor das medias
max_linhas = media_linhas.max()
max_colunas = media_colunas.max()

print("\nMaior média das linhas:", max_linhas)
print("Maior média das colunas:", max_colunas)

# Contagem de aparições
valores, contagens = np.unique(matriz, return_counts=True)
print("\nContagem de aparições (número: vezes):")
for v, c in zip(valores, contagens):
    print(f"{v}: {c}x")

# Exibe os que aparecem apenas 2 vezes
print(valores[contagens == 2])