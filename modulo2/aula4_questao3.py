# 3) Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. 
# O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário. 
# Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a 
# quantidade de 3 produtos comprados e imprima ao final o preço total da compra. 
# Note no exemplo a seguir que:

# Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito).
# A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de milhar e duas casas decimais).
# Entrada:
# Digite o nome do produto 1: calça
# Digite o preço unitário do produto 1: 199.90
# Digite a quantidade do produto 1: 3
# Digite o nome do produto 2: camisa
# Digite o preço unitário do produto 2: 49.95
# Digite a quantidade do produto 2: 10
# Digite o nome do produto 3: cinto
# Digite o preço unitário do produto 3: 25
# Digite a quantidade do produto 3: 3

# Saída:
# Total: R$1,174.20


## Entrada de dados 
input("Digite o nome do produto 1: ")
## Entrada de dados e processamento
valor_unit = float(input("Digite o preço unitário do produto 1: "))
## Entrada de dados e processamento
qtd = float(input("Digite a quantidade do produto 1: "))
## Processamento
orçamento_produto_1 = valor_unit * qtd


## Entrada de dados
input("Digite o nome do produto 2: ")
## Entrada de dados e processamento
valor_unit = float(input("Digite o preço unitário do produto 2: "))
## Entrada de dados e processamento
qtd = float(input("Digite a quantidade do produto 2: "))
## Processamento
orçamento_produto_2 = valor_unit * qtd


## Entrada de dados
input("Digite o nome do produto 3: ")
## Entrada de dados e processamento
valor_unit = float(input("Digite o preço unitário do produto 3: "))
## Entrada de dados e processamento
qtd = float(input("Digite a quantidade do produto 3: "))
## Processamento
orçamento_produto_3 = valor_unit * qtd


## Processamento
valor_total = orçamento_produto_1 + orçamento_produto_2 + orçamento_produto_3
## Saída
print(f"Total: R${valor_total:,.2f}")