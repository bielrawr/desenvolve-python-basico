# 1) Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17). 
# Escreva um programa que solicite as idades de Juliana e Cris e imprima True se ambas forem maiores de 17 anos, 
# indicando que podem entrar no bar, e False caso contrário.

# Entrada de dados e processamento
idade_ju = int(input("Juliana, por favor, digite sua idade: "))
# Entrada de dados e processamento
idade_cris = int(input("Cris, por favor, digite sua idade: "))
# Saída     ## variável(ju) é maior ou igual a 18 ((E)) variável(cris) é maior ou igual a 18 - se sim (True) senão (False)
print(idade_ju >=18 and idade_cris >= 18)
