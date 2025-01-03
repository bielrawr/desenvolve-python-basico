# Gerar uma lista com 20 elementos entre -10 e 10
import random
lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

# Encontrar o maior intervalo consecutivo com números negativos
max_inicial, max_final, max_tamanho = 0, 0, 0
inicial = 0

while inicial < len(lista):
    if lista[inicial] < 0:
        final = inicial
        while final < len(lista) and lista[final] < 0:
            final += 1
        tamanho = final - inicial
        if tamanho > max_tamanho:
            max_inicial, max_final, max_tamanho = inicial, final, tamanho
        inicial = final
    else:
        inicial += 1

# Deletar o maior intervalo consecutivo de números negativos
del lista[max_inicial:max_final]

print("Editada:", lista)
