
# 4) Escreva um programa que leia um valor inteiro referente a uma quantia em reais e 
# calcule a menor quantidade possível de notas necessárias para pagar aquele valor. 
# As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada exatamente como indicado. 

# Entrada:
# 576

# Saída:
# 5 nota(s) de R$100,00
# 1 nota(s) de R$50,00
# 1 nota(s) de R$20,00
# 0 nota(s) de R$10,00
# 1 nota(s) de R$5,00
# 0 nota(s) de R$2,00
# 1 nota(s) de R$1,00

## Entrada 
valor = int(input("Digite o valor a ser pago: "))

# Processamento
### maior nota (100)
nota_100 = valor // 100
### Atualização da var (valor)
valor = valor % 100
### prox maior nota (50)
nota_50 = valor // 50
### Atualização da var (valor)
valor = valor % 50

### prox maior nota (20)
nota_20 = valor // 20
### Atualização da var (valor)
valor = valor % 20

### prox maior nota (10)
nota_10 = valor // 10
### Atualização da var (valor)
valor = valor % 10

### prox maior nota (5)
nota_5 = valor // 5
### Atualização da var (valor)
valor = valor % 5

### prox maior nota (2)
nota_2 = valor // 2
### Atualização da var (valor)
valor = valor % 2 

nota_1 = valor

# Saída 
print(f"{nota_100} nota(s) de R$100,00")
print(f"{nota_50} nota(s) de R$50,00")
print(f"{nota_20} nota(s) de R$20,00")
print(f"{nota_10} nota(s) de R$10,00")
print(f"{nota_5} nota(s) de R$5,00")
print(f"{nota_2} nota(s) de R$2,00")
print(f"{nota_1} nota(s) de R$1,00")

