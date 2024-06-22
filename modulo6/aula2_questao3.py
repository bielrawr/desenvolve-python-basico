# 3) Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. 
# Crie uma terceira lista chamada interseccao contendo apenas os valores que se repetem nas duas listas. 
# Ao final imprima:
# Ambas as listas
# A lista intersecção ordenada
# A quantidade de vezes que cada elemento aparece em cada lista

import random

lista1, lista2 = [random.randint(0, 50) for _ in range(20)], [random.randint(0, 50) for _ in range(20)]
interseccao = []
for elemento in lista1:
    if elemento in lista2 and elemento not in interseccao:
        interseccao.append(elemento)

interseccao.sort()
print(lista1)
print(lista2)
print(interseccao)
for i in interseccao: print(i, lista1.count(i)), lista2.count(i)

