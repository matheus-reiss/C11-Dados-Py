import numpy as np
import random

# Matriz 2 por 2 de zeros
tabuleiro = np.zeros((2, 2), dtype=int)

# Adiciona o 1 em posição aleatoria
linha = random.randint(0, 1)
coluna = random.randint(0, 1)
tabuleiro[linha, coluna] = 1

# User tem até 3 tentativas
tentativas = 0
acertou = False

while tentativas < 3:
    print("\nJogada", tentativas + 1)
    l = int(input("Digite a linha (0 ou 1): "))
    c = int(input("Digite a coluna (0 ou 1): "))

    if tabuleiro[l, c] == 1:
        print("💥 Game Over :( Try Again!")
        acertou = True
        break
    else:
        print("Posição segura!")

    tentativas += 1

# Se não acertar a bomba em 3 jogadas
if not acertou:
    print("🎉 Congratulations! You beat the game! :)")