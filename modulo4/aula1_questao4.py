n = int(input("Insira o valor de N: "))
maior = 0
while n > 0:
    x = int(input("Insira o valor de X: "))
    if x > maior:
        maior = x
        n -= 1
    else:
        n -= 1
print(f"O maior valor é {maior}")