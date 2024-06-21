## Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e 
## calcule a raíz quadrada da soma dos valores. 
# Peça ao usuário o valor de n

import random
import math

n = int(input("Digite a quantidade de valores: "))
soma = 0
for i in range(n):
    valor = random.randint(0, 100)
    print(valor)
    soma += valor
print(soma)
print("A raíz quadrada é: " , math.sqrt(soma))