def intercalar_listas(lista1, lista2):
    tamanho1 = len(lista1)
    tamanho2 = len(lista2)
    resultado = []
    indice1 = 0
    indice2 = 0


    while indice1 < tamanho1 and indice2 < tamanho2:
        resultado.append(lista1[indice1])
        resultado.append(lista2[indice2])
        indice1 += 1
        indice2 += 1

    while indice1 < tamanho1:
        resultado.append(lista1[indice1])
        indice1 += 1

 

    while indice2 < tamanho2:
        resultado.append(lista2[indice2])
        indice2 += 1

    return resultado


def ler_lista():
    lista = []
    while True:
        elemento = input("Digite um número (ou deixe em branco para parar): ")
        if elemento == "":
            break
        lista.append(int(elemento))
    return lista


print("Digite os elementos da primeira lista (digite em branco para parar):")
lista1 = ler_lista()

print("\nDigite os elementos da segunda lista (digite em branco para parar):")
lista2 = ler_lista()


lista_intercalada = intercalar_listas(lista1, lista2)


print("\nLista intercalada:", lista_intercalada)
