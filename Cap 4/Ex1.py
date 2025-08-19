import numpy as np

# Criando os arrays
a = np.ones(8, dtype=int)
b = np.random.randint(0,10, size=8)

c = a + b

print("Array A:", a)
print("Array B:", b)
print("Array C (soma):", c)

#Verifica soma
soma = c.sum()
print("Soma total:", soma)

#Reshape
if soma >= 40:
    c = c.reshape(4,2)
else:
    c = c.reshape(2,4)

print("Matriz final:\n", c)