# 1) Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. 
# Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar. 
# Lembre-se do operador do python % que retorna o resto de uma divisão.


## Entrada
numero = int(input("Insira um valor: ")) + int(input("Insira um valor: "))
## Processamento
if numero % 2 == 0:
    ## Saída e impressão
    print("É par")
else:
    ## Saída e impressão
    print("É ímpar")
    
    