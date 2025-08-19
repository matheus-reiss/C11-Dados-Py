import numpy as np

# Array de pares 0 a 51 de 2 em 2 
a = np.arange(0,52,2)

# Array de pares 100 a 50 decrescendo de 2 em 2
b = np.arange(100,49,-2)

# Concatena
c = np.concatenate((a,b))

# Ordena em ordem crescente
c_ordenado = np.sort(c)

print("Array A:",a)
print("Array B:",b)
print("Concatenado:",c)
print("Ordenado:",c_ordenado)