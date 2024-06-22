# 1) Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os 
# armazene em uma lista. Em seguida imprima na ordem estabelecida:
# A lista ordenada, sem modificar a lista original
# A lista original
# O índice do maior valor da lista
# O índice do menor valor da lista

import random

valores = []
valores = [random.randint(-100, 100) for _ in range (20)]
print(sorted(valores))
print(valores)
print(valores.index(max(valores)))
print(valores.index(min(valores)))