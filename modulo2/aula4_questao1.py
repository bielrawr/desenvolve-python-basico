
# 1) Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), 
# bem como o preço do metro quadrado da região em ponto flutuante. Calcule o valor do terreno e 
# imprima o resultado com a formatação apresentada a seguir.

# O terreno possui 250m2 e custa R$512,490.50
#Comente na linha acima de cada instrução uma breve descrição da instrução.

#Fórmulas:
#area_m2 = comprimento * largura
#preco_total = preco_m2 * area_m2 

## Solicitação de entrada de dados - O comprimento do terreno em metros - Entrada
comprimento = int(input("Quantos metros de comprimento o terreno possui? : "))

## Solicitação de entrada de dados - A largura do terreno em metros - Entrada
largura = int(input("Quantos metros de largura o terreno possui? : "))

## Solicitação de entrada de dados - O valor do m2 na região - Entrada
preco_m2 = float(input("Qual o valor do m2? : "))

## Definição da variável e seu respectivo valor de acordo com o cálculo do comprimento e largura - Processamento
area_m2 = comprimento * largura

## Definição da variável e seu respectivo valor de acordo com o cálculo do preço do m2 e área do terreno - Processamento
preco_total = preco_m2 * area_m2

## Impressão do resultado com a formatação requerida - Saída
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")


